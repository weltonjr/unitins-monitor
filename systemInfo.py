import winstats


meminfo = winstats.get_mem_info()
print('    Total: %s b' % meminfo.TotalPhys)
print('    usage: %s%%' % meminfo.MemoryLoad)
print

pinfo = winstats.get_perf_info()
print('    Cache: %s p' % pinfo.SystemCache)
print('    Cache: %s b' % pinfo.SystemCacheBytes)
print()

drives = winstats.get_drives()
drive1 = drives[0]
fsinfo = winstats.get_fs_usage(drive1)
vinfo = winstats.get_vol_info(drive1)

print('    Disks:', ', '.join(drives))
print('    %s:\\' % drive1)
print('        Name:', vinfo.name)
print('        Type:', vinfo.fstype)
print('        Total:', fsinfo.total)
print('        Used: ', fsinfo.used)
print('        Free: ', fsinfo.free)
print()

