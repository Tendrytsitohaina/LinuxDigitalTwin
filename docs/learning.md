# Phase 1 core Systeme Linux

## System Information (cmd: uname)
les 3 repertoire 
/etc -> contient la configuration du systeme et des logiciel
    etc/os-release
    etc/passwd
    etc/hostname
    Donc /etc repond au comment le systeme ete configuree

/proc -> Informations du noyau et des processus
    Contient des nombre PID des processuss
    cat /proc/version
    cat /proc/uptime
    cat /proc/meminfo
    cat /proc/cpuinfo
    /proc = Que se passe-t-il actuellement dans le système ?

/sys information materielle
    /sys = Comment le kernel représente le matériel et les périphériques ?