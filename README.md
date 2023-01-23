# Threading investigation summary

As a result, we get two programs that perform the same action, namely, download 60 photos of very cute cats and save them to a folder on the disk.

### Sync

The result of executing the synchronous version will be 60 photos of cats, which were downloaded in 214.3523 seconds (in my case. it may be different for you, it also depends on the speed of the Internet).

The full log can be seen at [logs](sync_option.log).

### Thread

The result of running the version using threads will be 60 photos of cats, which were downloaded in 143.7893 seconds (in my case, yours may be different, also depends on the speed of the Internet).

The full log can be seen at [logs](threads_option.log).

## Conclusion

Using threads in this case made the program one and a half times faster.

## How to run?

**To run these files and verify the correctness of the programs yourself, you can use the following commands**:

### Sync program

on **macOS**/**linux**:

```
python3 sync_option.py
```

on **windows**:

```
python sync_option.py
```

### Thread program

on **macOS**/**linux**:

```
python3 threads_option.py
```

on **windows**:

```
python threads_option.py
```
