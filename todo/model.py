import string
import datetime


class TodoModel:
    id: int
    title: string
    description: string
    finished_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    def __init__(self,
                 id: int = None,
                 title: string = None,
                 description: string = None,
                 finished_at: datetime = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 deleted_at: datetime = None
                 ):
        self.id = id
        self.title = title
        self.description = description
        self.finished_at = finished_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
