from typing import List
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser


class ColorSettings(BaseModel):
    red: int
    green: int
    blue: int
    brightness: int


class LightSettings(BaseModel):
    light_name: str
    color: ColorSettings

    def dict(self, **kwargs):
        base_dict = super().dict(**kwargs)
        base_dict["color"] = self.color.dict(**kwargs)
        return base_dict


class LightScene(BaseModel):
    name: str
    description: str
    settings: List[LightSettings]


class LightConfigJsonParser:
    def __init__(self, json: str):
        parser = PydanticOutputParser(pydantic_object=LightScene)
        self._output = parser.parse(json)

    @property
    def output(self):
        return self._output.dict()
