check_if_connected_via_iphone
--------------------------------------------------

A simple script to check if you are connected to the
Internet with your iPhone (on Mac).

Can be used then from a bash script like this:

```bash
function check_if_via_lte {
	 lte=`check_if_connected_via_iphone.py`
	 if [ "$lte" == "True" ]; then
	     echo 'LTE detected, dont backup!'
	     exit
	 fi
}
```
