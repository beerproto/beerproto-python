# beerproto-python

Python protobuf bindings for [BeerProto](https://github.com/beerproto/beerproto) — a beer recipe format written in [Protocol Buffers](https://protobuf.dev/).

BeerProto is an alternative to formats like BeerXML and BeerJSON for describing beer recipes: ingredients, mash and boil steps, fermentation, packaging, styles, and the measurable units that tie them together. This library provides the generated Python message classes for the `beerproto.v1` schema so you can build, validate, serialize, and parse recipes in Python.

## Installation

```bash
pip install git+https://github.com/beerproto/beerproto-python.git
```

`protobuf` is installed automatically. The `buf.validate` schema types the messages
depend on are vendored into the package, so importing and using the messages needs
nothing else.

To enforce the schema's `protovalidate` constraints at runtime, install the optional
`validation` extra:

```bash
pip install "beerproto[validation] @ git+https://github.com/beerproto/beerproto-python.git"
```

## Usage

Messages live under the `beerproto.v1` package, one module per `.proto` file (suffixed `_pb2`):

```python
from beerproto.v1 import recipe_pb2

recipe = recipe_pb2.RecipeType(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="Pale Ale",
    type=recipe_pb2.RECIPE_UNIT_ALL_GRAIN,
)

# Serialize to bytes
data = recipe.SerializeToString()

# Parse from bytes
parsed = recipe_pb2.RecipeType()
parsed.ParseFromString(data)
```

The schema declares `protovalidate` constraints (e.g. `id` must be a UUID). To enforce
them at runtime, install the `validation` extra and call:

```python
import protovalidate

protovalidate.validate(recipe)  # raises ValidationError on invalid data
```

> **Note:** `protovalidate` is tightly coupled to a specific `buf.validate` schema
> version. The vendored `buf.validate` types come from beerproto's `buf.lock`; if your
> installed `protovalidate` expects a newer schema, validation may error even though
> the messages themselves serialize fine. Keep beerproto's `buf.lock` in step with the
> `protovalidate` release you target.

## Available modules

The `beerproto.v1` package includes `recipe`, `beer`, `style`, `hop`, `fermentable`, `culture`, `misc`, `water`, `mash`, `boil`, `fermentation`, `equipment`, `packaging`, `timing`, `srm`, `measureable_units`, and their step/graphic/vessel variants. Each ships with a `.pyi` stub for type checking.

## How this library is generated

This repository is generated, not hand-written. A [GitHub Actions workflow](.github/workflows/main.yml) checks out the [beerproto](https://github.com/beerproto/beerproto) schema and runs [Buf](https://buf.build/) with the Python template and `--include-imports`, so the imported `buf.validate` types are generated alongside the beerproto messages. The generated `beerproto/` and `buf/` trees are moved into this repo and pushed back. To reproduce locally:

```bash
buf generate beerprotoapis --template=buf.gen.python.yaml --include-imports
```

## License

See [LICENSE](LICENSE).
