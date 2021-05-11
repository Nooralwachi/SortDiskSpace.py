from collections import defaultdict
def SortDiskSpace(filename1, filename2):
    servers= defaultdict(float)
    usage_servers= {}
    with open(filename1, "r") as file1,open(filename2, "r") as file2:
        file1.readline()
        file2.readline()
        for line in file2:
            name, date,total= line.split()
            servers[name]=float(total)
        print(servers)
        for line in file1:
            name, cell,space= line.split()
            if name in servers.keys():
                usage_servers[name] = float(space)*100/float(servers[name])
        print(usage_servers)
        sorted_servers=sorted(usage_servers.items(), key=lambda x:x[1])
        for server, usage in sorted_servers:
            print(f'{server}')


SortDiskSpace("file_df1.txt", "file_df2.txt")
