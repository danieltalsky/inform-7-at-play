/* Minimal mkstemp adapter for the native Windows console build. */
#include <errno.h>
#include <fcntl.h>
#include <io.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>

int mkstemp(char *template_name)
{
    if (_mktemp_s(template_name, strlen(template_name) + 1) != 0) {
        errno = EINVAL;
        return -1;
    }
    return _open(template_name, _O_CREAT | _O_EXCL | _O_RDWR | _O_BINARY,
                 _S_IREAD | _S_IWRITE);
}
