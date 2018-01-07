import time

def checkUserData(params,idx,JSONstore,timeStamp):
    """
    :param params: parameters such as ID, name, location , postalCode that are used in order to retrieve a user using 'get' command
    :param idx: list of indices of matching users
    :param JSONstore: Contains all JSON documents
    :param timeStamp: Contains the timestamp for document creation
    :return: a list of users that satisfy the constraints in the 'get' command
    """
    values = [x for x in JSONstore.keys()]

    for val in values:

        try:
            if type(int(params[0])) == int:
                idx.append(params[0])
                break
        except ValueError:
            r = len(params)
            flag = []

            for i in range(0,r):
                if params[i] in JSONstore[val]:
                    flag.append(True)
                else:
                    flag.append(False)

            if False not in flag:
                idx.append(val)

    return_list = list(set(idx))
    return return_list

def insert(query,JSONstore,timeStamp):

    """
    :param query: query parameters to insert records to JSONstore
    :return: null
    """
    if query.__contains__('location'):
        data = query.strip('add ')
        if query.__contains__('location'):
            query = query.strip('add ').strip('}').strip(' {').replace('"','').replace('location:{','').replace('}','').split(',')
        else:
            query = query.strip('add ').strip('}').strip(' {').replace('"','').replace('}','').split(',')

        _id = query[0].split(':')[1]
        JSONstore[_id] = data
        timeStamp[_id] = time.time()

    elif query.__contains__('type'):
        data = query.split(':')[-1].rstrip('}')

        lines = map(str,data.split('\n'))
        for l in lines:
            global list_counter
            list_counter += 1
            JSONstore[str(list_counter)] = query.strip('add ')
            timeStamp[str(list_counter)] = time.time()
    else:
        data = query.strip('add ')
        query = query.strip('add ').strip('}').strip(' {').replace('"','').replace('}','').split(',')

        _id = query[0].split(':')[1]
        JSONstore[_id] = data
        timeStamp[_id] = time.time()

def get(query,JSONstore,timeStamp):

    """
    :param query: query parameters for 'get' command
    :return: matching records
    """
    if query.__contains__('type'):
        return_list = []
        search_params = query.strip('get ').strip('}').strip(' {').replace('"','').replace('}','')
        creation = {}

        for k,v in zip(JSONstore.keys(),JSONstore.values()):
            if search_params.split('[')[1][:-1] in v:
                #print k,v
                creation[k] = timeStamp[k]

        for key, value in sorted(creation.iteritems(), key=lambda (k,v): (v,k)):
            return_list.append(key)

        for i in return_list:
            print JSONstore[i]

        print '\n\n'

    elif query.__contains__('get '):

        params = []
        idx = []
        if query.__contains__('location'):
            search_params = query.strip('get ').strip('}').strip(' {').replace('"','').replace('location:{','').replace('}','').split(',')
        else:
            search_params = query.strip('get ').strip('}').strip(' {').replace('"','').replace('}','').split(',')

        for item in search_params:
            params.append(item.split(':')[1])

        return_list = checkUserData(params,idx,JSONstore,timeStamp)

        creation = {}
        for item in return_list:
            creation[item] = timeStamp[item]

        return_list = []
        for key, value in sorted(creation.iteritems(), key=lambda (k,v): (v,k)):
            return_list.append(key)

        for item in return_list:
            print JSONstore[item]

        print '\n\n'

def delete(query,JSONstore,timeStamp):

    """
    :param query: query parameters for delete command
    :return: deletes records based on parameters provided
    """
    params = []
    idx = []
    if query.__contains__('location'):
        search_params = query.strip('delete ').strip('}').strip(' {').replace('"','').replace('location:{','').replace('}','').split(',')
    else:
        search_params = query.strip('delete ').strip('}').strip(' {').replace('"','').replace('}','').split(',')

    for item in search_params:
        params.append(item.split(':')[1])

    return_list = checkUserData(params,idx,JSONstore,timeStamp)

    for item in return_list:
        del JSONstore[item]
        del timeStamp[item]


def main():

    JSONstore = {}
    timeStamp = {}
    global list_counter
    list_counter = 0

    lines = get_queries()

    for ip in lines:
        if ip[0] == 'a':
            insert(ip,JSONstore,timeStamp)
        if ip[0] == 'g':
            if ip[0] == 'g' and ip[5] == '}':
                for key, value in sorted(timeStamp.iteritems(), key=lambda (k,v): (v,k)):
                    print JSONstore[key]
            else:
                get(ip,JSONstore,timeStamp)
        elif ip[0] == 'd':
            delete(ip,JSONstore,timeStamp)

def get_queries():
    """
    :return: returns lines of queries to the main() function
    """
    lines = []
    line = raw_input()
    while line:
        try:
            lines.append(line)
            line = raw_input()
        except EOFError:
            break
    return lines


if __name__ == '__main__':
    main()




