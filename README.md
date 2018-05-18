# FireWheel

We live in a Post GDPR-mageddon; Fire and Wheel bring light and rainbows to the previously soul-crushing work of redacting Personal Identifiable Information (PII) commonly found in log files, and other unstructured text. Yeah. I'm looking at YOU, Splunk. To whit, we have invented Fire, and The Wheel.

FIRE! Are you worried about being sued for Billions of €uros under GDPR? Ya got email addresses in a logfile? We feel ya. Who doesn't? Kill 'em with FIRE.

WHEEL is vapourware. Now that we've cleared that up, this what it is gonna do: WHEEL will run over stuff like civic addresses and birthdays, leaving a clean conscience in its wake.

## Fire Features
- FIRE is gentle. It doesn't change the structure or content of a file other than redacting email addresses
- FIRE is robust. It has been tested extensively against massive datasets.
- FIRE is smart. It is clever enough to ignore image files (png and jpg) with a naming convention that resembles an email `e.g. imagefile@2x.png`


## Requirements
You must have Python 3.6 or higher. If not, you do not get into the club.

You will need the following (MIT licensed) 3rd party python modules:
 - The excellent `arrow` for better time handling than the built-in python modules
 - The equally excellent `tqdm` for totally awesome progress bars

## Caveats
Any email using the following [RFC 5322](https://tools.ietf.org/html/rfc5322) legal email characters/formats will NOT be anonymized by FireWheel.

- Consecutive quoted dots `e.g. John..Doe@example.com is not allowed but "John..Doe"@example.com is allowed`

- space and ` " ( ) , : ; < > @ [ \ ] ` characters inside a quoted-string (RFC 5322 3.2.4)

- email addresses with a backslash or double-quote preceded by a backslash

- email addresses with comments in parentheses at either end of the local-part; `e.g. john.smith(comment)@example.com and (comment)john.smith@example.com are both equivalent to john.smith@example.com`

- email addresses that contain the following characters, which are more commonly found in URLs as delimiters than in email addresses: `& ; / " < > ? $ =`. Please see table below that illustrates collisions between possible (legal) email address characters and possible URL delimiters (both official, and non-offical, but commonly used).

## Conflicts between emaill addresses and URLs
||A-Z|a-z|0-9|-|=|!|@|#|$|%|^|&|*|(|)|_|+|`|;|'|,|.|/|{|}|:|"|<|>|?|\||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
|legal in email addresses|x|x|x|x|x|x||x|x|x|x|x|x|||x|x|x|x|x||x|x|x|x|||||x|x|
|legal in URL without encoding|x|x|x|x|x|x|||x||||x|x|x|x|x|||x|x|x|||||||||
|used as delimiter in email (reserved)|||||||x|||||||x|x||||||||||||x|x|x||
|used as delimiters in URLs (reserved)|||||||x|||||x|||||||x||||x|||x|x|x|x|x|
|**conflict when parsing for email addresses**|||||**x**||**x**|||||**x**|||||||**x**||||**x**||||**x**|**x**|**x**|**x**|

## In Summary:
FireWheel *will* find emaill addresses that use any alphanumeric character as well as the `backtick` or any one of the following characters in the local-part: `! # $ % ' * + - ^ _{ | } ~ .` followed by `@` or `%40`, followed by a legal hostname.

It *will not* find (and anonymize) email addresses that contain any other characters. It *wil* change `%40` to `@`. It *will not* convert any urlencoded text other than `%40`.

## License
Copyright (c) 2018 Adam Z. Wasserman, Neil Schwartzman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.