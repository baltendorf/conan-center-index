#include <iostream>

<<<<<<< HEAD
#include <opentracing/ext/tags.h>
=======
>>>>>>> 9c1208497de912c7055aea148626aabf1e7552d2
#include <opentracing/noop.h>
#include <opentracing/tracer.h>

using namespace opentracing;

int main(int argc, char *argv[])
{
  auto tracer = MakeNoopTracer();
  auto span = tracer->StartSpan("a");
  
  return 0;
}