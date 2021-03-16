from .AudioFile import AudioFile
from api import db, ma
from marshmallow import fields, validate, validates

class Song(AudioFile):
    __tablename__ = None
    __mapper_args__ = {
        'polymorphic_identity':'song'
    }

    def __repr__(self):
        return f"name: {self.name}, Audio type: {self.audio_type}, Uploaded:{self.uploaded_time}"

class SongSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'name', 'duration')
        model = Song
        load_instance = True
    
    id = fields.Integer(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    duration = fields.Integer(required=True, validate=validate.Range(min=0))