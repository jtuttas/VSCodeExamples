from ldap3 import Server, Connection, AUTO_BIND_NO_TLS, SUBTREE, ALL_ATTRIBUTES
 
def get_ldap_info(u):
    with Connection(Server('192.168.178.123', port=389, use_ssl=False),
                    auto_bind=AUTO_BIND_NO_TLS,
                    read_only=True,
                    check_names=True,
                    user='CN=admin,CN=Users,DC=tuttas,DC=de', password='admin') as c:
         
        c.search(search_base='DC=tuttas,DC=de',
                 search_filter='(&(samAccountName=' + u + '))',
                 search_scope=SUBTREE,
                 attributes=ALL_ATTRIBUTES,
                 get_operational_attributes=True)
 
    print(c.response_to_json())
    print(c.result)
 
get_ldap_info('fiae17a.mmusterm')