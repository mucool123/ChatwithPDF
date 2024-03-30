pip install -U langchain-community
import json
import os
import sys
import boto3

##will use Titan Embeddings to generate embeddings

from langchain.embeddings import BedrockEmbeddings

from langchain.llms.bedrock import Bedrock