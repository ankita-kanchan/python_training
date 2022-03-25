
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

<h1>Python RegEx</h1>
              
 <p class="editor-contents__short-description">In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).</p>
              
        
<span property="dc:title" content="Python RegEx" class="rdf-meta element-hidden"></span>
  
  
<p id="introduction">A <strong>Reg</strong>ular <strong>Ex</strong>pression (RegEx) is a sequence of characters that defines a search pattern. For example,</p>

<pre style="max-height: 600px;"><code class="python hljs">^a...s$</code></pre>

<p>The above code defines a RegEx pattern. The pattern is: <strong>any five letter string starting with <var>a</var> and ending with <var>s</var></strong>.</p>

<p>A pattern defined using RegEx can be used to match against a string.</p>

<div class="table-responsive"><table summary="RegEx Match" cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="5"><code>^a...s$</code></td>
			<td><code>abs</code></td>
			<td>No match</td>
		</tr><tr><td><code>alias</code></td>
			<td>Match</td>
		</tr><tr><td><code>abyss</code></td>
			<td>Match</td>
		</tr><tr><td><code>Alias</code></td>
			<td>No match</td>
		</tr><tr><td><code>An abacus</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p>Python has a module named <code>re</code> to work with RegEx. Here's an example:</p>

<div class="pre-code-wrapper"><div title="Click to copy" class="copy-code-button"></div><pre class="python-exec" style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">import</span> re

pattern = <span class="hljs-string">'^a...s$'</span>
test_string = <span class="hljs-string">'abyss'</span>
result = re.match(pattern, test_string)

<span class="hljs-keyword">if</span> result:
  <span class="hljs-keyword">print</span>(<span class="hljs-string">"Search successful."</span>)
<span class="hljs-keyword">else</span>:
  <span class="hljs-keyword">print</span>(<span class="hljs-string">"Search unsuccessful."</span>)	
</code></pre></div>

<p>Here, we used <code>re.match()</code> function to search <var>pattern</var> within the <var>test_string</var>. The method returns a match object if the search is successful. If not, it returns <code>None</code>.</p>

<hr><p>There are other several functions defined in the <var>re</var> module to work with RegEx. Before we explore that, let's learn about regular expressions themselves.</p>

<p>If you already know the basics of RegEx, jump to <a href="#python-regex">Python RegEx</a>.</p>

<hr><h2><a id="search-pattern" name="search-pattern"></a>Specify Pattern Using RegEx</h2>

<p>To specify regular expressions, metacharacters are used. In the above example, <code>^</code> and <code>$</code> are metacharacters.</p>

<hr><h3>MetaCharacters</h3>

<p>Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:</p>

<p><strong>[]</strong> <strong>.</strong> <strong>^</strong> <strong>$</strong> <strong>*</strong> <strong>+</strong> <strong>?</strong> <strong>{}</strong> <strong>()</strong> <strong>\</strong> <strong>|</strong></p>

<hr><p><strong><code style="font-size: 1em;">[]</code> - Square brackets</strong></p>

<p>Square brackets specifies a set of characters you wish to match.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="4"><code>[abc]</code></td>
			<td><code>a</code></td>
			<td>1 match</td>
		</tr><tr><td><code>ac</code></td>
			<td>2 matches</td>
		</tr><tr><td><code>Hey Jude</code></td>
			<td>No match</td>
		</tr><tr><td><code>abc de ca</code></td>
			<td>5 matches</td>
		</tr></tbody></table></div><p>Here, <code>[abc]</code> will match if the string you are trying to match contains any of the <code>a</code>, <code>b</code> or <code>c</code>.</p>

<p>You can also specify a range of characters using <code>-</code> inside square brackets.</p>

<ul><li><code>[a-e]</code> is the same as <code>[abcde]</code>.</li>
	<li><code>[1-4]</code> is the same as <code>[1234]</code>.</li>
	<li><code>[0-39]</code> is the same as <code>[01239]</code>.</li>
</ul><p>You can complement (invert) the character set by using caret <code>^</code> symbol at the start of a square-bracket.</p>

<ul><li><code>[^abc]</code> means any character except <var>a</var> or <var>b</var> or <var>c</var>.</li>
	<li><code>[^0-9]</code> means any non-digit character.</li>
</ul><hr><p><code>.</code> - <strong>Period</strong></p>

<p>A period matches any single character (except newline <code>'\n'</code>).</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="4"><code>..</code></td>
			<td><code>a</code></td>
			<td>No match</td>
		</tr><tr><td><code>ac</code></td>
			<td>1 match</td>
		</tr><tr><td><code>acd</code></td>
			<td>1 match</td>
		</tr><tr><td><code>acde</code></td>
			<td>2 matches (contains 4 characters)</td>
		</tr></tbody></table></div><hr><p><code>^</code> - <strong>Caret</strong></p>

<p>The caret symbol <code>^</code> is used to check if a string <strong>starts with</strong> a certain character.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>^a</code></td>
			<td><code>a</code></td>
			<td>1 match</td>
		</tr><tr><td><code>abc</code></td>
			<td>1 match</td>
		</tr><tr><td><code>bac</code></td>
			<td>No match</td>
		</tr><tr><td rowspan="2"><code>^ab</code></td>
			<td><code>abc</code></td>
			<td>1 match</td>
		</tr><tr><td><code>acb</code></td>
			<td>No match (starts with <code>a</code> but not followed by <code>b</code>)</td>
		</tr></tbody></table></div><hr><p><code>$</code> - <strong>Dollar</strong></p>

<p>The dollar symbol <code>$</code> is used to check if a string <strong>ends with</strong> a certain character.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>a$</code></td>
			<td><code>a</code></td>
			<td>1 match</td>
		</tr><tr><td><code>formula</code></td>
			<td>1 match</td>
		</tr><tr><td><code>cab</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>*</code> - <strong>Star</strong></p>

<p>The star symbol <code>*</code> matches <strong>zero or more occurrences</strong> of the pattern left to it.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="5"><code>ma*n</code></td>
			<td><code>mn</code></td>
			<td>1 match</td>
		</tr><tr><td><code>man</code></td>
			<td>1 match</td>
		</tr><tr><td><code>maaan</code></td>
			<td>1 match</td>
		</tr><tr><td><code>main</code></td>
			<td>No match (<code>a</code> is not followed by <code>n</code>)</td>
		</tr><tr><td><code>woman</code></td>
			<td>1 match</td>
		</tr></tbody></table></div><hr><p><code>+</code> - <strong>Plus</strong></p>

<p>The plus symbol <code>+</code> matches <strong>one or more occurrences</strong> of the pattern left to it.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="5"><code>ma+n</code></td>
			<td><code>mn</code></td>
			<td>No match (no <code>a</code> character)</td>
		</tr><tr><td><code>man</code></td>
			<td>1 match</td>
		</tr><tr><td><code>maaan</code></td>
			<td>1 match</td>
		</tr><tr><td><code>main</code></td>
			<td>No match (a is not followed by n)</td>
		</tr><tr><td><code>woman</code></td>
			<td>1 match</td>
		</tr></tbody></table></div><hr><p><code>?</code> - <strong>Question Mark</strong></p>

<p>The question mark symbol <code>?</code> matches <strong>zero or one occurrence</strong> of the pattern left to it.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="5"><code>ma?n</code></td>
			<td><code>mn</code></td>
			<td>1 match</td>
		</tr><tr><td><code>man</code></td>
			<td>1 match</td>
		</tr><tr><td><code>maaan</code></td>
			<td>No match (more than one <code>a</code> character)</td>
		</tr><tr><td><code>main</code></td>
			<td>No match (a is not followed by n)</td>
		</tr><tr><td><code>woman</code></td>
			<td>1 match</td>
		</tr></tbody></table></div><hr><p><code>{}</code> - <strong>Braces</strong></p>

<p>Consider this code: <code>{n,m}</code>. This means at least <var>n</var>, and at most <var>m</var> repetitions of the pattern left to it.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="4"><code>a{2,3}</code></td>
			<td><code>abc dat</code></td>
			<td>No match</td>
		</tr><tr><td><code>abc daat</code></td>
			<td>1 match (at <code>d<u>aa</u>t</code>)</td>
		</tr><tr><td><code>aabc daaat</code></td>
			<td>2 matches (at <code><u>aa</u>bc</code> and <code>d<u>aaa</u>t</code>)</td>
		</tr><tr><td><code>aabc daaaat</code></td>
			<td>2 matches (at <code><u>aa</u>bc</code> and <code>d<u>aaa</u>at</code>)</td>
		</tr></tbody></table></div><p>Let's try one more example. This RegEx <code>[0-9]{2, 4}</code> matches at least 2 digits but not more than 4 digits</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>[0-9]{2,4}</code></td>
			<td><code>ab123csde</code></td>
			<td>1 match (match at <code>ab<u>123</u>csde</code>)</td>
		</tr><tr><td><code>12 and 345673</code></td>
			<td>3 matches (<code><u>12</u></code>, <code><u>3456</u></code>, <code><u>73</u></code>)</td>
		</tr><tr><td><code>1 and 2</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>|</code> - <strong>Alternation</strong></p>

<p>Vertical bar <code>|</code> is used for alternation (<code>or</code> operator).</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>a|b</code></td>
			<td><code>cde</code></td>
			<td>No match</td>
		</tr><tr><td><code>ade</code></td>
			<td>1 match (match at <code><u>a</u>de</code>)</td>
		</tr><tr><td><code>acdbea</code></td>
			<td>3 matches (at <code><u>a</u>cd<u>b</u>e<u>a</u></code>)</td>
		</tr></tbody></table></div><p>Here, <code>a|b</code> match any string that contains either <var>a</var> or <var>b</var></p>

<hr><p><code>()</code> - <strong>Group</strong></p>

<p>Parentheses <code>()</code> is used to group sub-patterns. For example, <code>(a|b|c)xz</code> match any string that matches either <var>a</var> or <var>b</var> or <var>c</var> followed by <var>xz</var></p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>(a|b|c)xz</code></td>
			<td><code>ab xz</code></td>
			<td>No match</td>
		</tr><tr><td><code>abxz</code></td>
			<td>1 match (match at <code>a<u>bxz</u></code>)</td>
		</tr><tr><td><code>axz cabxz</code></td>
			<td>2 matches (at <code><u>axz</u>bc ca<u>bxz</u></code>)</td>
		</tr></tbody></table></div><hr><p><code>\</code> - <strong>Backslash</strong></p>

<p>Backlash <code>\</code> is used to escape various characters including all metacharacters. For example,</p>

<p><code>\$a</code> match if a string contains <code>$</code> followed by <code>a</code>. Here, <code>$</code> is not interpreted by a RegEx engine in a special way.</p>

<p>If you are unsure if a character has special meaning or not, you can put <code>\</code> in front of it. This makes sure the character is not treated in a special way.</p>

<hr><p><strong>Special Sequences</strong></p>

<p>Special sequences make commonly used patterns easier to write. Here's a list of special sequences:</p>

<p></p><div id="block-inject-1" class="block-inject block-inject-1">
    
    
    
    <style>
    #div-gpt-ad-Programizcom37046 {display:none; width: 728px; height: 90px; }
    #div-gpt-ad-Programizcom36796 {display: block;}
    @media(min-width: 992px) { #div-gpt-ad-Programizcom37046 {display: block;} #div-gpt-ad-Programizcom36796 {display: none;}}
    </style><div class="pgAdWrapper" style="min-width: 728px; min-height: 90px; display: flex; justify-content: center; align-items: center;"><div id="div-gpt-ad-Programizcom37046" style="margin: 32px 0;">
    <div></div></div><div class="adSpinner" style="width: 60px; height: 60px; text-align: center; line-height: 60px; margin: 10px auto; font-size: 12px; position: absolute; display: none;"><span style="color: rgb(243, 243, 243);">Ad</span></div></div>
    
    <div id="div-gpt-ad-Programizcom36796" style="margin: 32px 0; min-height: 250px;">
    </div>
    </div><div class="clearfix"></div><p><code>\A</code> - Matches if the specified characters are at the start of a string.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="2"><code>\Athe</code></td>
			<td><code>the sun</code></td>
			<td>Match</td>
		</tr><tr><td><code>In the sun</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\b</code> - Matches if the specified characters are at the beginning or end of a word.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>\bfoo</code></td>
			<td><code>football</code></td>
			<td>Match</td>
		</tr><tr><td><code>a football</code></td>
			<td>Match</td>
		</tr><tr><td><code>afootball</code></td>
			<td>No match</td>
		</tr><tr><td rowspan="3"><code>foo\b</code></td>
			<td><code>the foo</code></td>
			<td>Match</td>
		</tr><tr><td><code>the afoo test</code></td>
			<td>Match</td>
		</tr><tr><td><code>the afootest</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\B</code> - Opposite of <code>\b</code>. Matches if the specified characters are <strong>not</strong> at the beginning or end of a word.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>\Bfoo</code></td>
			<td><code>football</code></td>
			<td>No match</td>
		</tr><tr><td><code>a football</code></td>
			<td>No match</td>
		</tr><tr><td><code>afootball</code></td>
			<td>Match</td>
		</tr><tr><td rowspan="3"><code>foo\B</code></td>
			<td><code>the foo</code></td>
			<td>No match</td>
		</tr><tr><td><code>the afoo test</code></td>
			<td>No match</td>
		</tr><tr><td><code>the afootest</code></td>
			<td>Match</td>
		</tr></tbody></table></div><hr><p><code>\d</code> - Matches any decimal digit. Equivalent to <code>[0-9]</code></p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="2"><code>\d</code></td>
			<td><code>12abc3</code></td>
			<td>3 matches (at <code><u>12</u>abc<u>3</u></code>)</td>
		</tr><tr><td><code>Python</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\D</code> - Matches any non-decimal digit. Equivalent to <code>[^0-9]</code></p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="2"><code>\D</code></td>
			<td><code>1ab34"50</code></td>
			<td>3 matches (at <code>1<u>ab</u>34<u>"</u>50</code>)</td>
		</tr><tr><td><code>1345</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\s</code> - Matches where a string contains any whitespace character. Equivalent to <code>[ \t\n\r\f\v]</code>.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="2"><code>\s</code></td>
			<td><code>Python RegEx</code></td>
			<td>1 match</td>
		</tr><tr><td><code>PythonRegEx</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\S</code> - Matches where a string contains any non-whitespace character. Equivalent to <code>[^ \t\n\r\f\v]</code>.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="2"><code>\S</code></td>
			<td><code>a b</code></td>
			<td>2 matches (at <code> <u>a</u> <u>b</u></code>)</td>
		</tr><tr><td><code>&nbsp;&nbsp;&nbsp;</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\w</code> - Matches any alphanumeric character (digits and alphabets). Equivalent to <code>[a-zA-Z0-9_]</code>. By the way, underscore <code>_</code> is also considered an alphanumeric character.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="2"><code>\w</code></td>
			<td><code>12&amp;": ;c </code></td>
			<td>3 matches (at <code><u>12</u>&amp;": ;<u>c</u></code>)</td>
		</tr><tr><td><code>%"&gt; !</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\W</code> - Matches any non-alphanumeric character. Equivalent to <code>[^a-zA-Z0-9_]</code></p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="2"><code>\W</code></td>
			<td><code>1a2%c</code></td>
			<td>1 match (at <code>1<u>a</u>2<u>%</u>c</code>)</td>
		</tr><tr><td><code>Python</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><code>\Z</code> - Matches if the specified characters are at the end of a string.</p>

<div class="table-responsive"><table cellspacing="1" cellpadding="1" border="0"><thead><tr><th scope="col">Expression</th>
			<th scope="col">String</th>
			<th scope="col">Matched?</th>
		</tr></thead><tbody><tr><td rowspan="3"><code>Python\Z</code></td>
			<td><code>I like Python</code></td>
			<td>1 match</td>
		</tr><tr><td><code>I like Python Programming</code></td>
			<td>No match</td>
		</tr><tr><td><code>Python is fun.</code></td>
			<td>No match</td>
		</tr></tbody></table></div><hr><p><strong>Tip:</strong> To build and test regular expressions, you can use RegEx tester tools such as <a href="https://regex101.com/" title="RegEx tester">regex101</a>. This tool not only helps you in creating regular expressions, but it also helps you learn it.</p>

<p>Now you understand the basics of RegEx, let's discuss how to use RegEx in your Python code.</p>

<hr><h2><a id="python-regex" name="python-regex"></a>Python RegEx</h2>

<p>Python has a module named <code>re</code> to work with regular expressions. To use it, we need to import the module.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">import</span> re</code></pre>

<p>The module defines several functions and constants to work with RegEx.</p>

<hr><h2><a id="re.findall" name="re.findall"></a>re.findall()</h2>

<p>The <code>re.findall()</code> method returns a list of strings containing all matches.</p>

<hr><h3>Example 1: re.findall()</h3>

<pre style="max-height: 600px;"><code class="python hljs">
<span class="hljs-comment"># Program to extract numbers from a string</span>

<span class="hljs-keyword">import</span> re

string = <span class="hljs-string">'hello 12 hi 89. Howdy 34'</span>
pattern = <span class="hljs-string">'\d+'</span>

result = re.findall(pattern, string) 
<span class="hljs-keyword">print</span>(result)

<span class="hljs-comment"># Output: ['12', '89', '34']</span>
</code></pre>

<p>If the pattern is not found, <code>re.findall()</code> returns an empty list.</p>

<hr><h2><a id="re.split" name="re.split"></a>re.split()</h2>

<p>The <code>re.split</code> method splits the string where there is a match and returns a list of strings where the splits have occurred.</p>

<hr><h3>Example 2: re.split()</h3>

<div class="pre-code-wrapper"><div title="Click to copy" class="copy-code-button"></div><pre class="python-exec" style="max-height: 600px;"><code class="python hljs">
<span class="hljs-keyword">import</span> re

string = <span class="hljs-string">'Twelve:12 Eighty nine:89.'</span>
pattern = <span class="hljs-string">'\d+'</span>

result = re.split(pattern, string) 
<span class="hljs-keyword">print</span>(result)

<span class="hljs-comment"># Output: ['Twelve:', ' Eighty nine:', '.']</span>
</code></pre></div>

<p>If the pattern is not found, <code>re.split()</code> returns a list containing the original string.</p>

<hr><p>You can pass <code>maxsplit</code> argument to the <code>re.split()</code> method. It's the maximum number of splits that will occur.</p>

<div class="pre-code-wrapper"><div title="Click to copy" class="copy-code-button"></div><pre class="python-exec" style="max-height: 600px;"><code class="python hljs">
<span class="hljs-keyword">import</span> re

string = <span class="hljs-string">'Twelve:12 Eighty nine:89 Nine:9.'</span>
pattern = <span class="hljs-string">'\d+'</span>

<span class="hljs-comment"># maxsplit = 1</span>
<span class="hljs-comment"># split only at the first occurrence</span>
result = re.split(pattern, string, <span class="hljs-number">1</span>) 
<span class="hljs-keyword">print</span>(result)

<span class="hljs-comment"># Output: ['Twelve:', ' Eighty nine:89 Nine:9.']</span>
</code></pre></div>

<p>By the way, the default value of <code>maxsplit</code> is 0; meaning all possible splits.</p>

<hr><h2><a id="re.sub" name="re.sub"></a>re.sub()</h2>

<p>The syntax of <code>re.sub()</code> is:</p>

<pre style="max-height: 600px;"><code class="python hljs">re.sub(pattern, replace, string)</code></pre>

<p>The method returns a string where matched occurrences are replaced with the content of <var>replace</var> variable.</p>

<hr><h3>Example 3: re.sub()</h3>

<div class="pre-code-wrapper"><div title="Click to copy" class="copy-code-button"></div><pre class="python-exec" style="max-height: 600px;"><code class="python hljs">
<span class="hljs-comment"># Program to remove all whitespaces</span>
<span class="hljs-keyword">import</span> re

<span class="hljs-comment"># multiline string</span>
string = <span class="hljs-string">'abc 12\
de 23 \n f45 6'</span>

<span class="hljs-comment"># matches all whitespace characters</span>
pattern = <span class="hljs-string">'\s+'</span>

<span class="hljs-comment"># empty string</span>
replace = <span class="hljs-string">''</span>

new_string = re.sub(pattern, replace, string) 
<span class="hljs-keyword">print</span>(new_string)

<span class="hljs-comment"># Output: abc12de23f456</span>
</code></pre></div>

<p>If the pattern is not found, <code>re.sub()</code> returns the original string.</p>

<hr><p>You can pass <var>count</var> as a fourth parameter to the <code>re.sub()</code> method. If omited, it results to 0. This will replace all occurrences.</p>

<pre style="max-height: 600px;"><code class="python hljs">
<span class="hljs-keyword">import</span> re

<span class="hljs-comment"># multiline string</span>
string = <span class="hljs-string">'abc 12\
de 23 \n f45 6'</span>

<span class="hljs-comment"># matches all whitespace characters</span>
pattern = <span class="hljs-string">'\s+'</span>
replace = <span class="hljs-string">''</span>

new_string = re.sub(<span class="hljs-string">r'\s+'</span>, replace, string, <span class="hljs-number">1</span>) 
<span class="hljs-keyword">print</span>(new_string)

<span class="hljs-comment"># Output:</span>
<span class="hljs-comment"># abc12de 23</span>
<span class="hljs-comment"># f45 6</span>
</code></pre>

<hr><h2>re.subn()</h2>

<p>The <code>re.subn()</code> is similar to <code>re.sub()</code> except it returns a tuple of 2 items containing the new string and the number of substitutions made.</p>

<hr><h3>Example 4: re.subn()</h3>

<div class="pre-code-wrapper"><div title="Click to copy" class="copy-code-button"></div><pre class="python-exec" style="max-height: 600px;"><code class="python hljs">
<span class="hljs-comment"># Program to remove all whitespaces</span>
<span class="hljs-keyword">import</span> re

<span class="hljs-comment"># multiline string</span>
string = <span class="hljs-string">'abc 12\
de 23 \n f45 6'</span>

<span class="hljs-comment"># matches all whitespace characters</span>
pattern = <span class="hljs-string">'\s+'</span>

<span class="hljs-comment"># empty string</span>
replace = <span class="hljs-string">''</span>

new_string = re.subn(pattern, replace, string) 
<span class="hljs-keyword">print</span>(new_string)

<span class="hljs-comment"># Output: ('abc12de23f456', 4)</span>
</code></pre></div>

<hr><h2><a id="re.search" name="re.search"></a>re.search()</h2>

<p>The <code>re.search()</code> method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.</p>

<p>If the search is successful, <code>re.search()</code> returns a match object; if not, it returns <code>None</code>.</p>

<pre style="max-height: 600px;"><code class="python hljs">match = re.search(pattern, str)</code></pre>

<hr><h3>Example 5: re.search()</h3>

<div class="pre-code-wrapper"><div title="Click to copy" class="copy-code-button"></div><pre class="python-exec" style="max-height: 600px;"><code class="python hljs">
<span class="hljs-keyword">import</span> re

string = <span class="hljs-string">"Python is fun"</span>

<span class="hljs-comment"># check if 'Python' is at the beginning</span>
match = re.search(<span class="hljs-string">'\APython'</span>, string)

<span class="hljs-keyword">if</span> match:
  <span class="hljs-keyword">print</span>(<span class="hljs-string">"pattern found inside the string"</span>)
<span class="hljs-keyword">else</span>:
  <span class="hljs-keyword">print</span>(<span class="hljs-string">"pattern not found"</span>)  

<span class="hljs-comment"># Output: pattern found inside the string</span>
</code></pre></div>

<p>Here, <var>match</var> contains a match object.</p>

<hr><h2><a id="match-object" name="match-object"></a>Match object</h2>

<p>You can get methods and attributes of a match object using <a href="/python-programming/methods/built-in/dir">dir()</a> function.</p>

<p>Some of the commonly used methods and attributes of match objects are:</p>

<hr><h3>match.group()</h3>

<p>The <code>group()</code> method returns the part of the string where there is a match.</p>

<h3>Example 6: Match object</h3>

<div class="pre-code-wrapper"><div title="Click to copy" class="copy-code-button"></div><pre class="python-exec" style="max-height: 600px;"><code class="python hljs">
<span class="hljs-keyword">import</span> re

string = <span class="hljs-string">'39801 356, 2102 1111'</span>

<span class="hljs-comment"># Three digit number followed by space followed by two digit number</span>
pattern = <span class="hljs-string">'(\d{3}) (\d{2})'</span>

<span class="hljs-comment"># match variable contains a Match object.</span>
match = re.search(pattern, string) 

<span class="hljs-keyword">if</span> match:
  <span class="hljs-keyword">print</span>(match.group())
<span class="hljs-keyword">else</span>:
  <span class="hljs-keyword">print</span>(<span class="hljs-string">"pattern not found"</span>)

<span class="hljs-comment"># Output: 801 35</span>
</code></pre></div>

<p>Here, <var>match</var> variable contains a match object.</p>

<p>Our pattern <code>(\d{3}) (\d{2})</code> has two subgroups <code>(\d{3})</code> and <code>(\d{2})</code>. You can get the part of the string of these parenthesized subgroups. Here's how:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>match.group(<span class="hljs-number">1</span>)
<span class="hljs-string">'801'</span>

<span class="hljs-meta">&gt;&gt;&gt; </span>match.group(<span class="hljs-number">2</span>)
<span class="hljs-string">'35'</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>match.group(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)
(<span class="hljs-string">'801'</span>, <span class="hljs-string">'35'</span>)

<span class="hljs-meta">&gt;&gt;&gt; </span>match.groups()
(<span class="hljs-string">'801'</span>, <span class="hljs-string">'35'</span>)
</code></pre>

<hr><h3>match.start(), match.end() and match.span()</h3>

<p>The <code>start()</code> function returns the index of the start of the matched substring. Similarly, <code>end()</code> returns the end index of the matched substring.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>match.start()
<span class="hljs-number">2</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>match.end()
<span class="hljs-number">8</span></code></pre>

<p>The <code>span()</code> function returns a tuple containing start and end index of the matched part.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>match.span()
(<span class="hljs-number">2</span>, <span class="hljs-number">8</span>)</code></pre>

<hr><h3>match.re and match.string</h3>

<p>The <code>re</code> attribute of a matched object returns a regular expression object. Similarly, <code>string</code> attribute returns the passed string.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>match.re
re.compile(<span class="hljs-string">'(\\d{3}) (\\d{2})'</span>)

<span class="hljs-meta">&gt;&gt;&gt; </span>match.string
<span class="hljs-string">'39801 356, 2102 1111'</span>
</code></pre>

<hr><p>We have covered all commonly used methods defined in the <code>re</code> module. If you want to learn more, visit <a href="https://docs.python.org/3/library/re.html">Python 3 re module</a>.</p>

<hr><h3><a id="r-prefix" name="r-prefix"></a>Using r prefix before RegEx</h3>

<p>When <var>r</var> or <var>R</var> prefix is used before a regular expression, it means raw string. For example, <code>'\n'</code> is a new line whereas <code>r'\n'</code> means two characters: a backslash <code>\</code> followed by <code>n</code>.</p>

<p>Backlash <code>\</code> is used to escape various characters including all metacharacters. However, using <var>r</var> prefix makes <code>\</code> treat as a normal character.</p>

<hr><h3>Example 7: Raw string using r prefix</h3>

<pre style="max-height: 600px;"><code class="python hljs">
<span class="hljs-keyword">import</span> re

string = <span class="hljs-string">'\n and \r are escape sequences.'</span>

result = re.findall(<span class="hljs-string">r'[\n\r]'</span>, string) 
<span class="hljs-keyword">print</span>(result)

<span class="hljs-comment"># Output: ['\n', '\r']</span>
</code></pre>
  </div>

  

          
    
  
