#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
setuid(0);
system("/usr/bin/python /home/pi/Documents/Project/file_action.py");
return 0;
}
