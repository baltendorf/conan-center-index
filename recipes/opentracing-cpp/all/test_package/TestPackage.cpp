#include <iostream>

#include <opentracing/ext/tags.h>
#include <opentracing/noop.h>
#include <opentracing/tracer.h>

using namespace opentracing;

int main(int argc, char *argv[])
{
  auto tracer = MakeNoopTracer();
  auto span = tracer->StartSpan("a");
  
  return 0;
}