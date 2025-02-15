#!/bin/bash

# Define the directory containing your .proto files
PROTO_DIR="./protos"

# Define the output directory for the generated Python code
OUT_DIR="./src"

# Create the output directory if it doesn't exist
mkdir -p $OUT_DIR

# Generate Python gRPC code for each .proto file in the PROTO_DIR
for proto_file in $PROTO_DIR/*.proto; do
    python -m grpc_tools.protoc -I$PROTO_DIR --python_out=$OUT_DIR --grpc_python_out=$OUT_DIR $proto_file
done

echo "gRPC code generation completed."