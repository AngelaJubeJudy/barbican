# Copyright (c) 2015 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def get_private_key_pkcs8():
    """Returns a private key in PCKS#8 format

    This key was created by issuing the following openssl commands:

    openssl genrsa -out private.pem 2048
    openssl pkcs8 -topk8 -nocrypt -in private.pem -out private.pk8

    The byte string returned by this function is the contents
    of the private.pk8 file.
    """

    return """-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCza2VoDXmBUMmw
jFu9F6MM5q/AZ1WjnWA2YNdNy237TrGN/nobDDv8FBBpUPmHNZ04H1LyxFcP8ReF
rcIXpifsReu2lAWaqRPxovu5CuAhfecKv+RhjLVLJ0I+MZIb72ROKpfZTmb7dhlF
gGD3vkC51BCfhGVW35w52OY/23x5MeO4yvx5myPccnxMVQ42KuDrzKqjBlSjmBnc
pGYx0JgCT+syFmHsl8rOkqCPPFLo24YQn+4/pr1AYwaZAbMTl9zoLtEQj6sxScuH
cS9e8niptDxlsbLQgqGVaGdE117stC95QH7UvITbuYzdjZwBFc1Sgz8GZ/2hLSsH
ujJiIQcvAgMBAAECggEAMOlUKbuSpigp85Ev6Sqqbnfs7Zy+Ae6DLg/UYgbVIq9f
RABdtUXujFfD6ZIDlFKPW59ec4QG3/evm+e0g9HuDEE7cviDVphFMZhm2xkV5Mt3
0rxhPB6pxaUcL+w/kpH+XDjMUJdJB8A4P3Qx+xfIeWBQb8wd/ELVSgfRLRNeqYL0
0KXVs04/FOBEhqSiqi/oHYJ4gxNrSoINX71PHVbaEikIygzi4HZVyMut3LE6ceHz
fSj71ftn+Ui0TzkLOb+NoBP31haHC/sfCrpKg7QtUP9q9dRq6dZcI17q5d7oEdET
eDRKhT2vm7bx2bLGeF1w2H9B/V81upjiAah2RVnecQKBgQDsfHSjR1gd+SHw/2A9
SaXS1k9LeXLt+UbDQdbjYOsh5LoT+EN/utO70RyDYqjlhzqJzciKTuAW5SVPC6gQ
uCppA29Kntq7x1+Lw/4wG947poXb60tLdg3BK5mBFTORk5ATqAwVq7t+2NtS5S/J
unzs5xrRolDFnSX4KnvVl6Jj3QKBgQDCOXZTVXRPEFhnqnqLErZe6EJkySwG8wgt
OdCmr660bocY1i9vV+RaM1iARHX6u/suMhkz+3KRinzxIG5gQsyiWmTpFV298W9v
kRtmsCQDn2my90yv4e6sLI0ng7l/N3r7CwLLNIV/CqeyaN40suzE8AjgEga5jTua
6bP5m+x8ewKBgQCeuW3DxXfkLjnUumMK36qX11XDb5FvHjebiE5FsOBAkHdAPgp3
6ZqBXfoISSjZXakxotft1MDdPRGMe2NjTWjRsQd6iyJ+lHORqIusGJhRaxQ/Ji8U
R/k1ZSETnXpORD+YodrylKA0pDKY8dDgUfXVP8wlVg9mg3JfnYweMTdCVQKBgQCx
133iNmgmkTfxzGci+wJkitVohdA7mMOO7daBGnKlImOvuUd784XTlhpecNF6wi/w
D82GDKLOY3meLO0EVYYczxqBVqAccXtxM/RcJcMEUi6twcXFcuJhYvXpDbOHqlyA
jIeFW9U1C6OcOGvm40Lr3UKzMa5Yrtq6MW4ri7uSCwKBgQDfdqVjT4uXmGwOh1z4
Pzv6GCoc+6GobXg4DvvCUjP9MR+2+5sX0AY/f+aVCD05/Nj0RqpAwUc03zZU5ZtL
2uNe6XDjEugfFtlzea6+rbD6KpFS+nxPJA8YyWYRpNhpRWGWQakHedr3BtMtGs0h
pKNAQG72HKWtSfJQMXvn2RlicA==
-----END PRIVATE KEY-----"""


def get_private_key_der():
    """Returns a private key in DER format

    This key was created by issuing the following openssl commands:

    openssl genrsa -out private.pem 2048
    openssl rsa -in private.pem -outform DER -out private.der

    The byte string returned by this function is the contents
    of the private.der file.
    """
    key_der = (
        '\x30\x82\x04\xa5\x02\x01\x00\x02\x82\x01\x01\x00\xb3\x6b\x65'
        '\x68\x0d\x79\x81\x50\xc9\xb0\x8c\x5b\xbd\x17\xa3\x0c\xe6\xaf'
        '\xc0\x67\x55\xa3\x9d\x60\x36\x60\xd7\x4d\xcb\x6d\xfb\x4e\xb1'
        '\x8d\xfe\x7a\x1b\x0c\x3b\xfc\x14\x10\x69\x50\xf9\x87\x35\x9d'
        '\x38\x1f\x52\xf2\xc4\x57\x0f\xf1\x17\x85\xad\xc2\x17\xa6\x27'
        '\xec\x45\xeb\xb6\x94\x05\x9a\xa9\x13\xf1\xa2\xfb\xb9\x0a\xe0'
        '\x21\x7d\xe7\x0a\xbf\xe4\x61\x8c\xb5\x4b\x27\x42\x3e\x31\x92'
        '\x1b\xef\x64\x4e\x2a\x97\xd9\x4e\x66\xfb\x76\x19\x45\x80\x60'
        '\xf7\xbe\x40\xb9\xd4\x10\x9f\x84\x65\x56\xdf\x9c\x39\xd8\xe6'
        '\x3f\xdb\x7c\x79\x31\xe3\xb8\xca\xfc\x79\x9b\x23\xdc\x72\x7c'
        '\x4c\x55\x0e\x36\x2a\xe0\xeb\xcc\xaa\xa3\x06\x54\xa3\x98\x19'
        '\xdc\xa4\x66\x31\xd0\x98\x02\x4f\xeb\x32\x16\x61\xec\x97\xca'
        '\xce\x92\xa0\x8f\x3c\x52\xe8\xdb\x86\x10\x9f\xee\x3f\xa6\xbd'
        '\x40\x63\x06\x99\x01\xb3\x13\x97\xdc\xe8\x2e\xd1\x10\x8f\xab'
        '\x31\x49\xcb\x87\x71\x2f\x5e\xf2\x78\xa9\xb4\x3c\x65\xb1\xb2'
        '\xd0\x82\xa1\x95\x68\x67\x44\xd7\x5e\xec\xb4\x2f\x79\x40\x7e'
        '\xd4\xbc\x84\xdb\xb9\x8c\xdd\x8d\x9c\x01\x15\xcd\x52\x83\x3f'
        '\x06\x67\xfd\xa1\x2d\x2b\x07\xba\x32\x62\x21\x07\x2f\x02\x03'
        '\x01\x00\x01\x02\x82\x01\x00\x30\xe9\x54\x29\xbb\x92\xa6\x28'
        '\x29\xf3\x91\x2f\xe9\x2a\xaa\x6e\x77\xec\xed\x9c\xbe\x01\xee'
        '\x83\x2e\x0f\xd4\x62\x06\xd5\x22\xaf\x5f\x44\x00\x5d\xb5\x45'
        '\xee\x8c\x57\xc3\xe9\x92\x03\x94\x52\x8f\x5b\x9f\x5e\x73\x84'
        '\x06\xdf\xf7\xaf\x9b\xe7\xb4\x83\xd1\xee\x0c\x41\x3b\x72\xf8'
        '\x83\x56\x98\x45\x31\x98\x66\xdb\x19\x15\xe4\xcb\x77\xd2\xbc'
        '\x61\x3c\x1e\xa9\xc5\xa5\x1c\x2f\xec\x3f\x92\x91\xfe\x5c\x38'
        '\xcc\x50\x97\x49\x07\xc0\x38\x3f\x74\x31\xfb\x17\xc8\x79\x60'
        '\x50\x6f\xcc\x1d\xfc\x42\xd5\x4a\x07\xd1\x2d\x13\x5e\xa9\x82'
        '\xf4\xd0\xa5\xd5\xb3\x4e\x3f\x14\xe0\x44\x86\xa4\xa2\xaa\x2f'
        '\xe8\x1d\x82\x78\x83\x13\x6b\x4a\x82\x0d\x5f\xbd\x4f\x1d\x56'
        '\xda\x12\x29\x08\xca\x0c\xe2\xe0\x76\x55\xc8\xcb\xad\xdc\xb1'
        '\x3a\x71\xe1\xf3\x7d\x28\xfb\xd5\xfb\x67\xf9\x48\xb4\x4f\x39'
        '\x0b\x39\xbf\x8d\xa0\x13\xf7\xd6\x16\x87\x0b\xfb\x1f\x0a\xba'
        '\x4a\x83\xb4\x2d\x50\xff\x6a\xf5\xd4\x6a\xe9\xd6\x5c\x23\x5e'
        '\xea\xe5\xde\xe8\x11\xd1\x13\x78\x34\x4a\x85\x3d\xaf\x9b\xb6'
        '\xf1\xd9\xb2\xc6\x78\x5d\x70\xd8\x7f\x41\xfd\x5f\x35\xba\x98'
        '\xe2\x01\xa8\x76\x45\x59\xde\x71\x02\x81\x81\x00\xec\x7c\x74'
        '\xa3\x47\x58\x1d\xf9\x21\xf0\xff\x60\x3d\x49\xa5\xd2\xd6\x4f'
        '\x4b\x79\x72\xed\xf9\x46\xc3\x41\xd6\xe3\x60\xeb\x21\xe4\xba'
        '\x13\xf8\x43\x7f\xba\xd3\xbb\xd1\x1c\x83\x62\xa8\xe5\x87\x3a'
        '\x89\xcd\xc8\x8a\x4e\xe0\x16\xe5\x25\x4f\x0b\xa8\x10\xb8\x2a'
        '\x69\x03\x6f\x4a\x9e\xda\xbb\xc7\x5f\x8b\xc3\xfe\x30\x1b\xde'
        '\x3b\xa6\x85\xdb\xeb\x4b\x4b\x76\x0d\xc1\x2b\x99\x81\x15\x33'
        '\x91\x93\x90\x13\xa8\x0c\x15\xab\xbb\x7e\xd8\xdb\x52\xe5\x2f'
        '\xc9\xba\x7c\xec\xe7\x1a\xd1\xa2\x50\xc5\x9d\x25\xf8\x2a\x7b'
        '\xd5\x97\xa2\x63\xdd\x02\x81\x81\x00\xc2\x39\x76\x53\x55\x74'
        '\x4f\x10\x58\x67\xaa\x7a\x8b\x12\xb6\x5e\xe8\x42\x64\xc9\x2c'
        '\x06\xf3\x08\x2d\x39\xd0\xa6\xaf\xae\xb4\x6e\x87\x18\xd6\x2f'
        '\x6f\x57\xe4\x5a\x33\x58\x80\x44\x75\xfa\xbb\xfb\x2e\x32\x19'
        '\x33\xfb\x72\x91\x8a\x7c\xf1\x20\x6e\x60\x42\xcc\xa2\x5a\x64'
        '\xe9\x15\x5d\xbd\xf1\x6f\x6f\x91\x1b\x66\xb0\x24\x03\x9f\x69'
        '\xb2\xf7\x4c\xaf\xe1\xee\xac\x2c\x8d\x27\x83\xb9\x7f\x37\x7a'
        '\xfb\x0b\x02\xcb\x34\x85\x7f\x0a\xa7\xb2\x68\xde\x34\xb2\xec'
        '\xc4\xf0\x08\xe0\x12\x06\xb9\x8d\x3b\x9a\xe9\xb3\xf9\x9b\xec'
        '\x7c\x7b\x02\x81\x81\x00\x9e\xb9\x6d\xc3\xc5\x77\xe4\x2e\x39'
        '\xd4\xba\x63\x0a\xdf\xaa\x97\xd7\x55\xc3\x6f\x91\x6f\x1e\x37'
        '\x9b\x88\x4e\x45\xb0\xe0\x40\x90\x77\x40\x3e\x0a\x77\xe9\x9a'
        '\x81\x5d\xfa\x08\x49\x28\xd9\x5d\xa9\x31\xa2\xd7\xed\xd4\xc0'
        '\xdd\x3d\x11\x8c\x7b\x63\x63\x4d\x68\xd1\xb1\x07\x7a\x8b\x22'
        '\x7e\x94\x73\x91\xa8\x8b\xac\x18\x98\x51\x6b\x14\x3f\x26\x2f'
        '\x14\x47\xf9\x35\x65\x21\x13\x9d\x7a\x4e\x44\x3f\x98\xa1\xda'
        '\xf2\x94\xa0\x34\xa4\x32\x98\xf1\xd0\xe0\x51\xf5\xd5\x3f\xcc'
        '\x25\x56\x0f\x66\x83\x72\x5f\x9d\x8c\x1e\x31\x37\x42\x55\x02'
        '\x81\x81\x00\xb1\xd7\x7d\xe2\x36\x68\x26\x91\x37\xf1\xcc\x67'
        '\x22\xfb\x02\x64\x8a\xd5\x68\x85\xd0\x3b\x98\xc3\x8e\xed\xd6'
        '\x81\x1a\x72\xa5\x22\x63\xaf\xb9\x47\x7b\xf3\x85\xd3\x96\x1a'
        '\x5e\x70\xd1\x7a\xc2\x2f\xf0\x0f\xcd\x86\x0c\xa2\xce\x63\x79'
        '\x9e\x2c\xed\x04\x55\x86\x1c\xcf\x1a\x81\x56\xa0\x1c\x71\x7b'
        '\x71\x33\xf4\x5c\x25\xc3\x04\x52\x2e\xad\xc1\xc5\xc5\x72\xe2'
        '\x61\x62\xf5\xe9\x0d\xb3\x87\xaa\x5c\x80\x8c\x87\x85\x5b\xd5'
        '\x35\x0b\xa3\x9c\x38\x6b\xe6\xe3\x42\xeb\xdd\x42\xb3\x31\xae'
        '\x58\xae\xda\xba\x31\x6e\x2b\x8b\xbb\x92\x0b\x02\x81\x81\x00'
        '\xdf\x76\xa5\x63\x4f\x8b\x97\x98\x6c\x0e\x87\x5c\xf8\x3f\x3b'
        '\xfa\x18\x2a\x1c\xfb\xa1\xa8\x6d\x78\x38\x0e\xfb\xc2\x52\x33'
        '\xfd\x31\x1f\xb6\xfb\x9b\x17\xd0\x06\x3f\x7f\xe6\x95\x08\x3d'
        '\x39\xfc\xd8\xf4\x46\xaa\x40\xc1\x47\x34\xdf\x36\x54\xe5\x9b'
        '\x4b\xda\xe3\x5e\xe9\x70\xe3\x12\xe8\x1f\x16\xd9\x73\x79\xae'
        '\xbe\xad\xb0\xfa\x2a\x91\x52\xfa\x7c\x4f\x24\x0f\x18\xc9\x66'
        '\x11\xa4\xd8\x69\x45\x61\x96\x41\xa9\x07\x79\xda\xf7\x06\xd3'
        '\x2d\x1a\xcd\x21\xa4\xa3\x40\x40\x6e\xf6\x1c\xa5\xad\x49\xf2'
        '\x50\x31\x7b\xe7\xd9\x19\x62\x70')
    return key_der


def get_public_key_pem():
    """Returns a public key in PEM format

    This key was created by issuing the following openssl commands:

    openssl genrsa -out private.pem 2048
    openssl rsa -in private.pem -pubout > public.pem

    The byte string returned by this function is the contents
    of the public.pem file.
    """

    return """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs2tlaA15gVDJsIxbvRej
DOavwGdVo51gNmDXTctt+06xjf56Gww7/BQQaVD5hzWdOB9S8sRXD/EXha3CF6Yn
7EXrtpQFmqkT8aL7uQrgIX3nCr/kYYy1SydCPjGSG+9kTiqX2U5m+3YZRYBg975A
udQQn4RlVt+cOdjmP9t8eTHjuMr8eZsj3HJ8TFUONirg68yqowZUo5gZ3KRmMdCY
Ak/rMhZh7JfKzpKgjzxS6NuGEJ/uP6a9QGMGmQGzE5fc6C7REI+rMUnLh3EvXvJ4
qbQ8ZbGy0IKhlWhnRNde7LQveUB+1LyE27mM3Y2cARXNUoM/Bmf9oS0rB7oyYiEH
LwIDAQAB
-----END PUBLIC KEY-----"""


def get_public_key_der():
    """Returns a public key in DER format

    This key was created by issuing the following openssl commands:

    openssl genrsa -out private.pem 2048
    openssl rsa -in private.pem -pubout > public.pem

    The byte string returned by this function is the contents
    of the public.der file.
    """
    key_der = (
        '\x30\x82\x01\x22\x30\x0d\x06\x09\x2a\x86\x48\x86\xf7\x0d\x01'
        '\x01\x01\x05\x00\x03\x82\x01\x0f\x00\x30\x82\x01\x0a\x02\x82'
        '\x01\x01\x00\xb3\x6b\x65\x68\x0d\x79\x81\x50\xc9\xb0\x8c\x5b'
        '\xbd\x17\xa3\x0c\xe6\xaf\xc0\x67\x55\xa3\x9d\x60\x36\x60\xd7'
        '\x4d\xcb\x6d\xfb\x4e\xb1\x8d\xfe\x7a\x1b\x0c\x3b\xfc\x14\x10'
        '\x69\x50\xf9\x87\x35\x9d\x38\x1f\x52\xf2\xc4\x57\x0f\xf1\x17'
        '\x85\xad\xc2\x17\xa6\x27\xec\x45\xeb\xb6\x94\x05\x9a\xa9\x13'
        '\xf1\xa2\xfb\xb9\x0a\xe0\x21\x7d\xe7\x0a\xbf\xe4\x61\x8c\xb5'
        '\x4b\x27\x42\x3e\x31\x92\x1b\xef\x64\x4e\x2a\x97\xd9\x4e\x66'
        '\xfb\x76\x19\x45\x80\x60\xf7\xbe\x40\xb9\xd4\x10\x9f\x84\x65'
        '\x56\xdf\x9c\x39\xd8\xe6\x3f\xdb\x7c\x79\x31\xe3\xb8\xca\xfc'
        '\x79\x9b\x23\xdc\x72\x7c\x4c\x55\x0e\x36\x2a\xe0\xeb\xcc\xaa'
        '\xa3\x06\x54\xa3\x98\x19\xdc\xa4\x66\x31\xd0\x98\x02\x4f\xeb'
        '\x32\x16\x61\xec\x97\xca\xce\x92\xa0\x8f\x3c\x52\xe8\xdb\x86'
        '\x10\x9f\xee\x3f\xa6\xbd\x40\x63\x06\x99\x01\xb3\x13\x97\xdc'
        '\xe8\x2e\xd1\x10\x8f\xab\x31\x49\xcb\x87\x71\x2f\x5e\xf2\x78'
        '\xa9\xb4\x3c\x65\xb1\xb2\xd0\x82\xa1\x95\x68\x67\x44\xd7\x5e'
        '\xec\xb4\x2f\x79\x40\x7e\xd4\xbc\x84\xdb\xb9\x8c\xdd\x8d\x9c'
        '\x01\x15\xcd\x52\x83\x3f\x06\x67\xfd\xa1\x2d\x2b\x07\xba\x32'
        '\x62\x21\x07\x2f\x02\x03\x01\x00\x01')
    return key_der


def get_encrypted_private_key_pkcs8():
    """Returns an encrypted private key in PKCS#8 format

    This key was created by issuing the following openssl commands:

    openssl genrsa -out private.pem 2048
    echo password > passphrase.txt
    openssl pkcs8 -topk8 -passout file:passphrase.txt \
                  -in private.pem -out private_encrypted.pk8

    The byte string returned by this function is the contents
    of the private_encrypted.pk8 file.
    """

    return """-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIE6TAbBgkqhkiG9w0BBQMwDgQIssadeQrYhhACAggABIIEyDNw3SV2b19yy4Q/
kTbtJ/p2X2zKDqr7GgLeAowqqhcMfvprI7G8C0XtwxkR4SjMZUXNcmOwQB2kNKtK
ZilCz6pSx81iUj4s1fU460XkhkIeV+F7aB2PsTG1oDfPCuzKFjT6EuSE6lFUH89r
TRuHWMPseW7lrvEB5kNMFag5QxeKjsSCNkZWOT74o4fh3cEplgCEaA+nCclXU79m
5rhaa9e1SUpPuPlhnAIDkBtHcC38B+SOYKQxLdZT1f72oZ1ozWJ4bEhKxvnNu5J+
tCvgWOXMIEJVGgf8Cu58PoR18LyyAIk7zza+1LkCiyuLNgiz8a1sVw8uBcrVgD5R
8f4XgI/Yjb16Bmpp/0iEjNcURaby9GnCCEc+W/ivSJTnG3o1Xn00FO98l2aggNpt
S8gxK05NeCtdWoFFjTeIXxnb1ct0Iep8RwuO+FnupAf6aw12Uqj4qYNvNiY/kBhS
P/Yd3KznasrolUZ9+PVTMUI45UTMN/XhNvXrozMq9nItWTV7wHyEL3mrYipvcxrm
SnLlAp2zkmSu923cHN1teLE99/rV2jaBM03ROqvYWaxjfOjxfwz6PhdE8G//kWd0
tf2Om+fyCkBRxo1sUcuiE79hJXgP5KJCMbPsDyG/aQk4oeS1nbn15AhthwiU7A13
h9X6asgV2H+4Ljf+tr1b8p3qj3CSljfzoVErLqoHagjVB45WktHhrWbUSRpXSvPo
Hh0LY62qxTa67gKjwarH5hYr5IaH39iR9bcyuvzE+u9TJWvWmeLJ7UmesfVPZtSf
/JTpvr0zu4C95lXKt4FdxOhGcWwDN1Zp+lCsF5ruBGc+/pEggiXi1qvW9xUny1Of
8NqdPxGPb4/zPHGaysypPsc6LiY3esI8wa7FnDsS4e79dWinD/BPWEa5N2jLm0Rr
njkHTy0xtnw/a8Ofrtyy9V1tBBOCaswzGIZZj6oHyFCtAvjZuYa8TWVmSi6EqJKi
lY5wSdQQXg3H0HnQYivtOY1YbfjtRkUB9e4xkSVhvYJpY1QWBtApdUGBsxsELkDC
6cv/Kxnd9U7dz9+VhD0hAdrhFqbWqOEGTWt7xE44yzWokdKQWu5FsTs6gyXsGPen
ZgZlR5pjPNGbMdftW0M473YyvtzjrCuSVgJspCzpA9uo6wfejaFb4RF/tcWtXglE
Q5FzfsO1OZr6nONraShj9N1kxGBXUUOtAjZI/zoTWk3yndxw3IpvPtDTg9ByCp7F
RFUtDyrki+YAIAiTgPq7qwc1upjU7R1Zlg4jIe0RI9A73NyLwa4QhgO+HmRBt7At
LLuUeCFKuXMBHzlDaMYwq5ZPOb8VcMkhUoug2YJIc4YOOHh5O0mYnat0vaYO+A58
DiuYgxKmO5+6+OMk2ovZgk1sFawR4rk9HUt8goUUptZ+hoHUVGtte5YcQniIOcds
qY3ni/zwswHWQRaAu8Ej4qJKt1XwZo2K04xHhL90TMaY8NpLSMCfVqDDL409TqIj
zHUfYl6N2Me4eKc8vl6Sm63g57NzLqTttD6KSn8v+OmUF5mOQwcLnr3nK7S+BQfI
DLPY1Oh7Kec/M/d1080/Qv9YBAJhz50TLKoxXwVeH4OOvuaHVaotElMkr5QEkEXl
gRgwkbMrQjg0II0O9g==
-----END ENCRYPTED PRIVATE KEY-----"""


def get_passphrase_txt():
    """Returns the plain text string used to encrypt the private key

    This key was created by issuing the following commands:

    echo password > passphrase.txt

    The byte string returned by this function is the contents
    of the passphrase.txt file.
    """

    return """password"""


def get_csr_pem():
    """Returns a Certificate Signing Request (CSR) in PEM format

    This key was created by issuing the following openssl commands:

    openssl genrsa -out private.pem 2048
    openssl req -new -key private.pem -out csr.pem -subj '/CN=example.com'

    The byte string returned by this function is the contents
    of the csr.pem file.
    """

    return """-----BEGIN CERTIFICATE REQUEST-----
MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3
DQEBAQUAA4IBDwAwggEKAoIBAQCza2VoDXmBUMmwjFu9F6MM5q/AZ1WjnWA2YNdN
y237TrGN/nobDDv8FBBpUPmHNZ04H1LyxFcP8ReFrcIXpifsReu2lAWaqRPxovu5
CuAhfecKv+RhjLVLJ0I+MZIb72ROKpfZTmb7dhlFgGD3vkC51BCfhGVW35w52OY/
23x5MeO4yvx5myPccnxMVQ42KuDrzKqjBlSjmBncpGYx0JgCT+syFmHsl8rOkqCP
PFLo24YQn+4/pr1AYwaZAbMTl9zoLtEQj6sxScuHcS9e8niptDxlsbLQgqGVaGdE
117stC95QH7UvITbuYzdjZwBFc1Sgz8GZ/2hLSsHujJiIQcvAgMBAAGgADANBgkq
hkiG9w0BAQsFAAOCAQEAPJDIxzgtUDRgpfTbTOPDJYap+Lm4jYxsCuAFbYiQ43B+
c7RyzEFOB2anrldTm3XzNytHZAkRTnN4dH09p1K1Pyepv+weSv8rvN9OohfYgpcj
wQqw8ksdGb3Q6oPnTgGxmWvV4PbzHmDnOvOiQ+wuBHWXYks6tdgU7iCZ1djYibmL
1j+XEvtstou8gu1lWhzH6tStwmA9udncg5rEvfDUDyvMN3T06QFqrlK9K1TXIlbM
RvUDrBjINIOuEeZ/5czjBl1CX1Z1YqdunrPiCQM4+oUAtjyD6ZAsyAEXLKdSYtKZ
hSZgIl7v+UAIM+9bhpVg15aTjRzfH2OsZodFIbsMDw==
-----END CERTIFICATE REQUEST-----"""


def get_certificate_pem():
    """Returns an X509 certificate in PEM format

    This key was created by issuing the following openssl commands:

    openssl genrsa -out private.pem 2048
    openssl req -new -x509 -key private.pem -out cert.pem \
                -days 1000 -subj '/CN=example.com'

    The byte string returned by this function is the contents
    of the cert.pem file.
    """

    return """-----BEGIN CERTIFICATE-----
MIIC/zCCAeegAwIBAgIJAOLqXKJ9q9/nMA0GCSqGSIb3DQEBCwUAMBYxFDASBgNV
BAMMC2V4YW1wbGUuY29tMB4XDTE1MDQxMTAyMTUyOVoXDTE4MDEwNTAyMTUyOVow
FjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQCza2VoDXmBUMmwjFu9F6MM5q/AZ1WjnWA2YNdNy237TrGN/nobDDv8
FBBpUPmHNZ04H1LyxFcP8ReFrcIXpifsReu2lAWaqRPxovu5CuAhfecKv+RhjLVL
J0I+MZIb72ROKpfZTmb7dhlFgGD3vkC51BCfhGVW35w52OY/23x5MeO4yvx5myPc
cnxMVQ42KuDrzKqjBlSjmBncpGYx0JgCT+syFmHsl8rOkqCPPFLo24YQn+4/pr1A
YwaZAbMTl9zoLtEQj6sxScuHcS9e8niptDxlsbLQgqGVaGdE117stC95QH7UvITb
uYzdjZwBFc1Sgz8GZ/2hLSsHujJiIQcvAgMBAAGjUDBOMB0GA1UdDgQWBBSUq2A0
b2Xo+sKvmKgN8Wq8l6j82jAfBgNVHSMEGDAWgBSUq2A0b2Xo+sKvmKgN8Wq8l6j8
2jAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBjiuqhlzNVOVLrHDQy
Gr0fTACFJdDREnuhZp4d91++DmMCT+bcTG0+GCp3rfFOuEWpJLLLPdSOnIsnibsO
syKPXuBBX5kmdYIojbdjUTSwnhcx9JTAfKSmxXWSC0rnKCefAf44Mm6fqvoTyTbe
GSQP6nHzc7eLaK/efcrMvYdct+TeTkHjqR8Lu4pjZvRdUQadQHhDyN+ONKdKD9Tr
jvfPim0b7Aq885PjSN6Qo4Z9HXR6+nK+bTz9HyUATMfDGNQt0L3vyfVxbNOxkCBc
YI4hFtGfkOzd6B7r2sY1wGKdTLHkuT4m4/9A/SOzvnH+epnJqIS9jw+1iRj8xcDA
6PNT
-----END CERTIFICATE-----"""
