# Notes for CCDS

Course grade: Assignments (20%) + Project (40%) + Final Exam (40%)

### Create an Empty Hard Disk Image

    qemu-img create -f qcow2 debian-disk.qcow2 10G

### Boot from the Installation Image

    qemu-system-x86_64 -m 2048 -enable-kvm -cpu host -cdrom debian-mini.iso -boot d -drive file=debian-disk.qcow2,format=qcow2 -net nic -net user

### Boot the Installed OS

    qemu-system-x86_64 -m 2048 -enable-kvm -cpu host -drive file=debian-disk.qcow2,format=qcow2 -net nic -net user,hostfwd=tcp::2222-:22 &

### Some tips

* To SSH into the VM, you can set up a bridged network or use -net user,hostfwd=tcp::2222-:22 to forward ports and then access the VM via SSH on port 2222.

        ssh -p 2222 puput@localhost


* Create snapshots of your virtual disk image to preserve the state:

        qemu-img snapshot -c snapshotX debian-disk.qcow2
