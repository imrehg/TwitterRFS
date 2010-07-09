

As an excercise after reading a blogpost [Building Filesystems the Way You Build Web Apps](Building Filesystems the Way You Build Web Apps), Twitter-RouteFS (or TwitterRFS) is a simple, readonly filesystem to get tweets quickly in the filesystem and be able to interact with them in other programs that might not know how to access Twitter.

## Requirements
[python-fuse](http://pypi.python.org/pypi/fuse-python/0.2)
[python-routes](http://pypi.python.org/pypi/Routes)
[python-routefs](http://pypi.python.org/pypi/RouteFS)
[python-twitter](http://code.google.com/p/python-twitter/)

## Usage

    > chmod +x twitterrfs.py
    > mkdir twitter
    > ./twitterrfs.py twitter
    > ls twitter/
 
This should show an empty directory

    > ls twitter/<username>

This will list <username>'s tweets by their ID numbers. To see the tweet text, just issue:

    > cat twitter/<username>/<ID>

Also, now the username is known, so

    > ls twitter/
    <username>

The username and tweets are cached, thus not updated after the first check. Thus to update, now one has to remount.

    > fusermount -u twitter
    > ./twitterrfs.py twitter 

## Known issues

Because python-fuse don't seem to support unicode text in files, unicode tweets have to be escaped at the moment. This might make the text pretty much unreadable.

## License

Released under MIT-style license, for details see License.txt in the root directory.

