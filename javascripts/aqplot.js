$(function() {
	// check for hashbang
	if(window.location.hash) {
		// break hash
		hash = window.location.hash;
		hash = hash.replace('#','');
		hash = hash.split('&');
		for(rule in hash){
			rule = hash[rule];
			rule = rule.split('=');
			switch(rule[0]){
				case 'set-proxy':
					$.jStorage.set('proxy-location', rule[1]);
					console.log(rule[1]);
			}
		}

		
	}
});
