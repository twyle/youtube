from typing import Any

from ...models import CommentThread
from ...schemas import (
    CommentThreadFilter,
    CommentThreadOptionalParameters,
    CommentThreadPart,
    YouTubeListResponse,
    YouTubeRequest,
)
from ..resource import YouTubeResource


class YouTubeCommentThread(YouTubeResource):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__(youtube_client)
        self.request_schema: YouTubeRequest = None
        self.next_page_token: str = None

    def parse_author(self, comment_snippet: dict) -> dict:
        author: dict = dict()
        author['display_name'] = comment_snippet['authorDisplayName']
        author['profile_image_url'] = comment_snippet['authorProfileImageUrl']
        author['channel_url'] = comment_snippet['authorChannelUrl']
        author['channel_id'] = comment_snippet['authorChannelId']['value']
        return author

    def parse_toplevel_comment(self, top_level_comment: dict) -> dict:
        comment: dict = dict()
        snippet: dict = dict()
        snippet['author'] = self.parse_author(top_level_comment['snippet'])
        snippet['channel_id'] = top_level_comment['snippet']['channelId']
        snippet['video_id'] = top_level_comment['snippet']['videoId']
        snippet['text_display'] = top_level_comment['snippet']['textDisplay']
        snippet['text_original'] = top_level_comment['snippet']['textOriginal']
        snippet['can_rate'] = top_level_comment['snippet']['canRate']
        snippet['viewer_rating'] = top_level_comment['snippet']['viewerRating']
        snippet['like_count'] = top_level_comment['snippet']['likeCount']
        if top_level_comment['snippet'].get('moderationStatus'):
            snippet['moderation_status'] = top_level_comment['snippet'][
                'moderationStatus'
            ]
        else:
            comment['moderation_status'] = ''
        snippet['published_at'] = top_level_comment['snippet']['publishedAt']
        snippet['updated_at'] = top_level_comment['snippet']['updatedAt']
        if top_level_comment['snippet'].get('parentId'):
            snippet['parent_id'] = top_level_comment['snippet']['parentId']
        else:
            snippet['parent_id'] = None
        comment['snippet'] = snippet
        comment['id'] = top_level_comment['id']
        return comment

    def parse_snippets(self, snippet_data: dict[str, Any]) -> dict[str, Any]:
        parsed_snippet: dict[str, Any] = dict()
        parsed_snippet['channel_id'] = snippet_data['channelId']
        parsed_snippet['video_id'] = snippet_data.get('videoId', '')
        parsed_snippet['can_reply'] = snippet_data.get('canReply', True)
        parsed_snippet['is_public'] = snippet_data.get('isPublic', True)
        parsed_snippet['total_reply_count'] = snippet_data['totalReplyCount']
        parsed_snippet['top_level_comment'] = self.parse_toplevel_comment(
            snippet_data['topLevelComment']
        )
        return dict(snippet=parsed_snippet)

    def parse_item(self, item: dict) -> CommentThread:
        id_data: dict = self.parse_id(item)
        snippet_data: dict = self.parse_snippets(item['snippet'])
        id_data.update(snippet_data)
        return CommentThread(**id_data, replies=[])

    def parse_youtube_threadlist_response(
        self, youtube_list_response: dict
    ) -> YouTubeListResponse:
        youtube_result: YouTubeListResponse = YouTubeListResponse(
            kind=youtube_list_response['kind'],
            etag=youtube_list_response['etag'],
            items=self.parse_items(youtube_list_response['items']),
        )
        return youtube_result

    def find_video_comments(self, request: YouTubeRequest) -> YouTubeListResponse:
        """Get a particular video's comments."""
        comment_thread_req = self.youtube_client.commentThreads().list(
            **self.create_request_dict(request)
        )
        comment_thread_resp = comment_thread_req.execute()
        return self.parse_youtube_list_response(comment_thread_resp)

    def find_all_channel_comments(self, request: YouTubeRequest) -> YouTubeListResponse:
        """Get a particular channels's comments."""
        request_dict: dict = self.create_request_dict(request)
        find_channel_comments: dict = self.youtube_client.commentThreads().list(
            **request_dict
        )
        find_channel_comments_resp: dict = find_channel_comments.execute()
        return self.parse_youtube_list_response(find_channel_comments_resp)

    # TODO create a custom parser
    def get_comment(self, comment_id: str) -> YouTubeListResponse:
        request_filter: CommentThreadFilter = CommentThreadFilter(id=[comment_id])
        part: CommentThreadPart = CommentThreadPart(part=['id', 'snippet'])
        optional_params: CommentThreadOptionalParameters = (
            CommentThreadOptionalParameters()
        )
        youtube_request: YouTubeRequest = YouTubeRequest(
            part=part, filter=request_filter, optional_parameters=optional_params
        )
        request_dict = self.create_request_dict(youtube_request)
        find_comment_request: dict = self.youtube_client.comments().list(**request_dict)
        find_comment_result: dict = find_comment_request.execute()
        return find_comment_result

    # TODO create a custom parser
    def get_comments(self, comment_ids: list[str]) -> YouTubeListResponse:
        request_filter: CommentThreadFilter = CommentThreadFilter(id=comment_ids)
        part: CommentThreadPart = CommentThreadPart(part=['id', 'snippet'])
        optional_params: CommentThreadOptionalParameters = (
            CommentThreadOptionalParameters()
        )
        youtube_request: YouTubeRequest = YouTubeRequest(
            part=part, filter=request_filter, optional_parameters=optional_params
        )
        request_dict = self.create_request_dict(youtube_request)
        find_comment_request: dict = self.youtube_client.comments().list(**request_dict)
        find_comment_result: dict = find_comment_request.execute()
        return find_comment_result

    # TODO create a custom parser
    def get_comment_replies(self, comment_id: str) -> YouTubeListResponse:
        comment_reply_request = self.youtube_client.comments().list(
            part='snippet,id', parentId=comment_id
        )
        comment_reply_response = comment_reply_request.execute()
        return comment_reply_response
