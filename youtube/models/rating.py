from ..resources.schemas.resource_schema import Resource

class YouTubeVideoRating(Resource):
    video_id: str
    rating: str
