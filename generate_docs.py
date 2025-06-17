import subprocess
import json
from fastapi.openapi.utils import get_openapi
from src.main import app


def export_openapi_json():
    schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    with open("docs/openapi.json", "w") as f:
        json.dump(schema, f, indent=2)
    print("✅ Đã tạo openapi.json")


def generate_html():
    # subprocess.run(["redoc-cli", "bundle", "docs/openapi.json", "-o", "docs/docs.html"], shell=True, check=True)
    subprocess.run("npx @redocly/cli build-docs docs/openapi.json --output docs/docs.html", shell=True, check=True)
    print("✅ Đã tạo docs.html")


def generate_md():
    # subprocess.run(["widdershins", "docs/openapi.json", "-o", "docs/docs.md"], shell=True, check=True)
    subprocess.run( "widdershins --language_tabs=[] --code-samples=false --httpsnippet=false --omitHeader "
                    "docs/openapi.json -o "
                    "docs/docs.md",
                   shell=True, check=True)
    print("✅ Đã tạo docs.md")


if __name__ == "__main__":
    export_openapi_json()
    generate_html()
    generate_md()
