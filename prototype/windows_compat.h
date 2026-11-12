/* CheapGlk uses POSIX spellings; MinGW supplies most of them. */
#include <time.h>
#include <string.h>
int mkstemp(char *template_name);
#define timegm _mkgmtime
#define bzero(ptr, size) memset((ptr), 0, (size))
