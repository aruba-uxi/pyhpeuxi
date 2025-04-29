openapi-generator generate -i https://api.capenetworks.com/docs/openapi.yaml -g python -c config.json -o .
python -m tools.lint-attribution format
