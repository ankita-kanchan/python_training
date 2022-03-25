
<a href="https://docs.python.org/3/library/re.html">Python Regular Expression Documents</a>

<h4>Frequently Used Regular Expressions</h4>
<ol>
<li><b>^</b> matches the beginning of a string.</li>
<li><b>$</b> matches the end of a string.</li>
<li><b>\b</b> matches a word boundary.</li>
<li><b>\d</b> matches any numeric digit.</li>
<li><b>\D</b> matches any non-numeric character.</li>
<li><b>(x|y|z)</b> matches exactly one of <b>x</b>, <b>y</b> or <b>z</b>.</li>
<li><b>(x)</b> in general is a remembered group. We can get the value of what matched by using the <b>groups()</b> method of the object returned by <b>re.search</b>.</li>
<li><b>x?</b> matches an optional <b>x</b> character (in other words, it matches an <b>x</b> zero or one times).</li>
<li><b>x*</b> matches <b>x</b> zero or more times.</li>
<li><b>x+</b> matches <b>x</b> one or more times.</li>
<li><b>x{m,n}</b> matches an <strong>x</strong> character at least <strong>m</strong> times, but not more than <b>n</b> times.</li>
<li><b>?:</b> matches an expression but do not capture it. Non capturing group.</li>
<li><b>?=</b> matches a suffix but exclude it from capture. Positive look ahead. <br>
   a(?=b) will match the "a" in "ab", but not the "a" in "ac" <br>
   In other words, a(?=b) matches the "a" which is followed by the string 'b', without consuming what follows the a.
   </li>
<li><b>?!</b> matches if suffix is absent. Negative look ahead.<br>
   a(?!b) will match the "a" in "ac", but not the "a" in "ab"</li>
<li><b>?&lt;= </b> positive look behind</li>
<li><b>?&lt;! </b> negative look behind</li>
</ol>
