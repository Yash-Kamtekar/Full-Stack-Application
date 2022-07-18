from pydantic import BaseModel, EmailStr, Field

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")


class RegisterUser(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr = Field(...)
    password: str = Field(...)
    phone: str = Field(...)
    rewards: float= Field(...)
    role: str = Field(...)
    member_type: str = Field(...)

    # class Config:
    #     allow_population_by_field_name = True
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}
    #     # schema_extra = {
    #     #     "example": {
    #     #         "name": "Jane Doe",
    #     #         "email": "jdoe@example.com",
    #     #         "course": "Experiments, Science, and Fashion in Nanophotonics",
    #     #         "gpa": "3.0",
    #     #     }
    #     # }
class LoginUser(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)