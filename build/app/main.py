#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, File, UploadFile, Response
from pydantic import BaseModel
import html_gen


class Item(BaseModel):
    name: str


app = FastAPI()


@app.get("/")
def read_root():
    return Response(content=html_gen.homepage(), media_type="application/xml")


@app.post("/api/string/")
async def from_string(item: Item):
    return "1"


@app.post("/api/file/")
async def from_file(file: UploadFile = File(...)):
    return "2"
