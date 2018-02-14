var ActiveDirectory = require('activedirectory');
var config = {
    url: 'ldap://192.168.178.123:389',
    baseDN: 'dc=tuttas,dc=de',
    username: 'CN=admin,CN=Users,DC=tuttas,DC=de',
    password: 'admin'
}

var sAMAccountName = 'FIAE17A.tmusterf';

// Find user by a sAMAccountName
var ad = new ActiveDirectory(config);
ad.findUser(sAMAccountName, function (err, user) {
    if (err) {
        console.log('ERROR: ' + JSON.stringify(err));
        return;
    }

    if (!user) {
        console.log('User: ' + sAMAccountName + ' not found.');
    }
    else {
        console.log(JSON.stringify(user));
        if (user.dn.indexOf("OU=Lehrer") > -1) {
            console.log('Ist ein Lehrer');
        }
        else if (user.dn.indexOf("OU=Schüler") > -1) {
            console.log('Ist ein Schüler');
        }
    }
});