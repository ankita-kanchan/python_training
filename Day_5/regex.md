
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

<div class="right-bar">
                            
    
    
    
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

  
  
</div>

                  
                              <div class="tutorial-toc"><div class="tutorial-toc__inner"><h3 class="tutorial-toc__title">Table of Contents
      <button class="btn btn--clear align-items-center">
      <svg class="programiz-icon"><use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#x"></use></svg></button></h3><div class="tutorial-toc__links"><ul><li><a href="#introduction" class="">RegEx Introduction</a></li>
	<li><a href="#search-pattern" class="active">Create patterns using metacharacters</a></li>
	<li><a href="#python-regex">Python RegEx</a>
		<ul><li><a href="#re.findall">re.findall()</a></li>
			<li><a href="#re.split">re.split()</a></li>
			<li><a href="#re.sub">re.sub()</a></li>
			<li><a href="#re.search">re.search()</a></li>
			<li><a href="#match-object">Match object</a></li>
			<li><a href="#r-prefix">r Prefix before RegEx</a></li>
		</ul></li>
</ul></div></div></div>                          </div>

                          <div class="block">
                  
    
    
    
    

<div class="pagination-area">

    
        <div class="pagination-area__btn pagination-area__btn--prev">
            <a href="/python-programming/property" title="Python Property" class="btn pagination-btn d-flex align-items-center justify-content-end">
                <div class="btn__labels text-right">
                    <div class="btn__sub-label">Previous Tutorial:</div>
                    <div class="btn__label">Python Property</div>
                </div>
            </a></div>
    
    
        <div class="pagination-area__btn pagination-area__btn--next">

            <a href="/python-programming/examples" title="Python Examples" class="btn btn--primary pagination-btn d-flex align-items-center justify-content-end">
                <div class="btn__labels text-right">
                    <div class="btn__sub-label">Next Tutorial:</div>
                    <div class="btn__label">Python Examples</div>
                </div>
                <svg class="programiz-icon"><use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#arrow-right"></use></svg></a>
        </div>
    </div>
    
    
    
    
    <section class="vote-share-wrapper"><div class="share-wrapper">
        <span>Share on:</span>
        <div class="share-buttons-container">
            <div class="social-button-individual"><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.programiz.com/python-programming/regex"><svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333"></circle><path fill-rule="evenodd" clip-rule="evenodd" d="M18.9167 10.168H17.1667C15.5558 10.168 14.25 11.4738 14.25 13.0846V14.8346H12.5V17.168H14.25V21.8346H16.5833V17.168H18.3333L18.9167 14.8346H16.5833V13.0846C16.5833 12.7625 16.8445 12.5013 17.1667 12.5013H18.9167V10.168Z" stroke="#0556F3" stroke-width="1.16999" stroke-linecap="round" stroke-linejoin="round"></path></svg></a></div>
            <div class="social-button-individual"><a href="https://twitter.com/intent/tweet?text=Check%20this%20amazing%20article%20on%20Python%20RegEx:%20&amp;via=programiz&amp;url=https://www.programiz.com/python-programming/regex"><svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333"></circle><path fill-rule="evenodd" clip-rule="evenodd" d="M22.4167 10.7521C21.8581 11.1461 21.2396 11.4475 20.585 11.6446C19.8654 10.8171 18.7058 10.527 17.6813 10.918C16.6568 11.309 15.9853 12.2981 16 13.3946V13.9779C13.9179 14.0319 11.9471 13.0399 10.75 11.3354C10.75 11.3354 8.41671 16.5854 13.6667 18.9187C12.4653 19.7342 11.0342 20.1431 9.58337 20.0854C14.8334 23.0021 21.25 20.0854 21.25 13.3771C21.2495 13.2146 21.2339 13.0525 21.2034 12.8929C21.7987 12.3058 22.2189 11.5645 22.4167 10.7521Z" stroke="#0556F3" stroke-width="1.22222" stroke-linecap="round" stroke-linejoin="round"></path></svg></a></div>
            <div class="social-button-individual"><a href="https://api.whatsapp.com//send?text=Check+this+amazing+article+on+Python%20RegEx:+https://www.programiz.com/python-programming/regex"><svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333"></circle><path d="M21.0115 10.9885C19.7291 9.70613 18.0245 9 16.2108 9C16.2107 9 16.2103 9 16.2102 9C15.3132 9.00011 14.4391 9.17378 13.6122 9.51633C12.7853 9.85887 12.0445 10.3542 11.4101 10.9885C10.1278 12.2708 9.42169 13.9757 9.42169 15.7892C9.42169 16.8706 9.68263 17.9454 10.1771 18.9029L9.03589 22.163C8.95546 22.393 9.01239 22.6429 9.18479 22.8152C9.30538 22.9359 9.4641 23 9.62731 23C9.69727 23 9.76798 22.9883 9.83698 22.9641L13.0971 21.823C14.0546 22.3175 15.1294 22.5784 16.2108 22.5784C18.0243 22.5784 19.7291 21.8722 21.0115 20.5899C22.2938 19.3076 23 17.6027 23 15.7893C23 13.9757 22.2939 12.2708 21.0115 10.9885ZM20.4309 20.0093C19.3037 21.1366 17.8049 21.7572 16.2108 21.7572C15.2357 21.7572 14.2669 21.5161 13.4092 21.0596C13.2537 20.9769 13.0698 20.9627 12.9048 21.0205L9.94293 22.0571L10.9796 19.0952C11.0374 18.9299 11.0231 18.7461 10.9404 18.5907C10.484 17.7332 10.2428 16.7645 10.2428 15.7892C10.2428 14.1951 10.8635 12.6963 11.9907 11.5691C13.1178 10.4421 14.6164 9.82127 16.2103 9.82106H16.2108C17.805 9.82106 19.3037 10.4418 20.4309 11.5691C21.5582 12.6963 22.1789 14.195 22.1789 15.7892C22.1789 17.3833 21.5582 18.8821 20.4309 20.0093Z" fill="#0556F3" stroke="#0556F3" stroke-width="0.3"></path><path d="M18.734 16.3976C18.4216 16.0853 17.9134 16.0853 17.6011 16.3976L17.2595 16.7392C16.4113 16.277 15.725 15.5906 15.2627 14.7424L15.6043 14.4009C15.9167 14.0885 15.9167 13.5803 15.6043 13.268L14.6838 12.3475C14.3715 12.0352 13.8633 12.0352 13.5509 12.3475L12.8146 13.0839C12.3928 13.5057 12.3717 14.2308 12.7553 15.1258C13.0883 15.9028 13.6978 16.7569 14.4714 17.5305C15.2451 18.3042 16.0991 18.9137 16.8762 19.2467C17.3014 19.4289 17.6882 19.5198 18.0224 19.5198C18.3916 19.5198 18.6967 19.4088 18.9181 19.1874L19.6545 18.4509V18.451C19.8058 18.2997 19.8891 18.0986 19.8891 17.8846C19.8891 17.6706 19.8058 17.4695 19.6545 17.3182L18.734 16.3976ZM18.3375 18.6068C18.2171 18.7272 17.8469 18.7693 17.1997 18.4921C16.5163 18.1992 15.7536 17.6515 15.0521 16.9499C14.3505 16.2484 13.8029 15.4857 13.51 14.8024C13.2326 14.1552 13.2748 13.7849 13.3952 13.6645L14.1175 12.9422L15.0096 13.8344L14.582 14.2621C14.3887 14.4554 14.342 14.7486 14.466 14.9917C15.0281 16.094 15.9079 16.9738 17.0102 17.536C17.2535 17.66 17.5466 17.6134 17.74 17.42L18.1675 16.9924L19.0597 17.8846L18.3375 18.6068Z" fill="#0556F3" stroke="#0556F3" stroke-width="0.3"></path></svg></a></div>
            <div class="social-button-individual"><a href="https://www.linkedin.com/sharing/share-offsite/?url=https://www.programiz.com/python-programming/regex"><svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333"></circle><path d="M13.3748 14.5417V20.375C13.3748 20.4524 13.3441 20.5265 13.2894 20.5812C13.2347 20.6359 13.1605 20.6667 13.0832 20.6667H11.6248C11.5475 20.6667 11.4733 20.6359 11.4186 20.5812C11.3639 20.5265 11.3332 20.4524 11.3332 20.375V14.5417C11.3332 14.4643 11.3639 14.3901 11.4186 14.3354C11.4733 14.2807 11.5475 14.25 11.6248 14.25H13.0832C13.1605 14.25 13.2347 14.2807 13.2894 14.3354C13.3441 14.3901 13.3748 14.4643 13.3748 14.5417ZM21.2498 16.8225C21.2596 16.2095 21.0596 15.6115 20.683 15.1277C20.3063 14.644 19.7757 14.3034 19.179 14.1625C18.773 14.0751 18.352 14.0861 17.9511 14.1947C17.5502 14.3033 17.1812 14.5063 16.8748 14.7867V14.5417C16.8748 14.4643 16.8441 14.3901 16.7894 14.3354C16.7347 14.2807 16.6605 14.25 16.5832 14.25H15.1248C15.0475 14.25 14.9733 14.2807 14.9186 14.3354C14.8639 14.3901 14.8332 14.4643 14.8332 14.5417V20.375C14.8332 20.4524 14.8639 20.5265 14.9186 20.5812C14.9733 20.6359 15.0475 20.6667 15.1248 20.6667H16.5832C16.6605 20.6667 16.7347 20.6359 16.7894 20.5812C16.8441 20.5265 16.8748 20.4524 16.8748 20.375V17.085C16.8679 16.8012 16.9611 16.524 17.1382 16.3021C17.3153 16.0802 17.5649 15.9278 17.8432 15.8717C18.0121 15.8425 18.1854 15.8509 18.3507 15.8964C18.516 15.9418 18.6693 16.0231 18.7996 16.1345C18.93 16.2459 19.0341 16.3846 19.1047 16.5408C19.1754 16.697 19.2107 16.8669 19.2082 17.0383V20.375C19.2082 20.4524 19.2389 20.5265 19.2936 20.5812C19.3483 20.6359 19.4225 20.6667 19.4998 20.6667H20.9582C21.0355 20.6667 21.1097 20.6359 21.1644 20.5812C21.2191 20.5265 21.2498 20.4524 21.2498 20.375V16.8225ZM12.2082 10.75C11.9774 10.75 11.7519 10.8184 11.56 10.9466C11.3681 11.0748 11.2186 11.257 11.1303 11.4702C11.042 11.6834 11.0189 11.918 11.0639 12.1443C11.1089 12.3706 11.2201 12.5785 11.3832 12.7416C11.5464 12.9048 11.7543 13.0159 11.9806 13.0609C12.2069 13.1059 12.4415 13.0828 12.6546 12.9945C12.8678 12.9062 13.05 12.7567 13.1782 12.5648C13.3064 12.373 13.3748 12.1474 13.3748 11.9167C13.3748 11.6072 13.2519 11.3105 13.0331 11.0917C12.8143 10.8729 12.5176 10.75 12.2082 10.75Z" fill="#0556F3"></path></svg></a></div>
        </div>
    </div>
    <div class="vote-wrapper">
        <span>Did you find this article helpful?</span>
        <div class="vote-container" data-nid="1495">
            <div class="vote-up">
                <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18 36C27.9411 36 36 27.9411 36 18C36 8.05887 27.9411 0 18 0C8.05887 0 0 8.05887 0 18C0 27.9411 8.05887 36 18 36Z" fill="#FFCC4D"></path><path d="M18.0005 21.0014C14.3775 21.0014 11.9735 20.5794 9.00049 20.0014C8.32149 19.8704 7.00049 20.0014 7.00049 22.0014C7.00049 26.0014 11.5955 31.0014 18.0005 31.0014C24.4045 31.0014 29.0005 26.0014 29.0005 22.0014C29.0005 20.0014 27.6795 19.8694 27.0005 20.0014C24.0275 20.5794 21.6235 21.0014 18.0005 21.0014Z" fill="#664500"></path><path d="M9.00049 22C9.00049 22 12.0005 23 18.0005 23C24.0005 23 27.0005 22 27.0005 22C27.0005 22 25.0005 26 18.0005 26C11.0005 26 9.00049 22 9.00049 22Z" fill="white"></path><path d="M12.0017 17C13.3824 17 14.5017 15.433 14.5017 13.5C14.5017 11.567 13.3824 10 12.0017 10C10.621 10 9.50171 11.567 9.50171 13.5C9.50171 15.433 10.621 17 12.0017 17Z" fill="#664500"></path><path d="M24.0002 17C25.381 17 26.5002 15.433 26.5002 13.5C26.5002 11.567 25.381 10 24.0002 10C22.6195 10 21.5002 11.567 21.5002 13.5C21.5002 15.433 22.6195 17 24.0002 17Z" fill="#664500"></path></svg></div>
            <div class="vote-down">
                <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18 36C27.9411 36 36 27.9411 36 18C36 8.05887 27.9411 0 18 0C8.05887 0 0 8.05887 0 18C0 27.9411 8.05887 36 18 36Z" fill="#FFCC4D"></path><path d="M25.4849 27.3751C25.4399 27.1961 24.3169 22.9961 17.9999 22.9961C11.6819 22.9961 10.5599 27.1961 10.5149 27.3751C10.4599 27.5921 10.5579 27.8171 10.7519 27.9291C10.9469 28.0401 11.1909 28.0071 11.3519 27.8521C11.3709 27.8331 13.3059 25.9961 17.9999 25.9961C22.6939 25.9961 24.6299 27.8331 24.6479 27.8511C24.7439 27.9461 24.8719 27.9961 24.9999 27.9961C25.0839 27.9961 25.1689 27.9751 25.2459 27.9321C25.4419 27.8201 25.5399 27.5931 25.4849 27.3751Z" fill="#664500"></path><path d="M12.0024 17C13.3832 17 14.5024 15.433 14.5024 13.5C14.5024 11.567 13.3832 10 12.0024 10C10.6217 10 9.50244 11.567 9.50244 13.5C9.50244 15.433 10.6217 17 12.0024 17Z" fill="#664500"></path><path d="M24.0005 17C25.3812 17 26.5005 15.433 26.5005 13.5C26.5005 11.567 25.3812 10 24.0005 10C22.6198 10 21.5005 11.567 21.5005 13.5C21.5005 15.433 22.6198 17 24.0005 17Z" fill="#664500"></path></svg></div>
        </div>
    </div>
        <div class="page-feedback-form" style="display: none;">
        <form class="webform-client-form webform-client-form-1680" action="/python-programming/regex" method="post" id="webform-client-form-1680" accept-charset="UTF-8"><div><div class="form-item webform-component webform-component-markup webform-component--page-feedback-header">
 <p class="font-weight-600" style="font-size: 18px;">Sorry about that.</p>
<label class="social-area__label" style="margin-top: 20px; font-size: 14px;">How can we improve it?</label>
</div>
<div class="rate-share-form"><div class="col-md-12"><div class="form"><div class="form-item webform-component webform-component-textarea webform-component--dislike-feedback">
  <label class="element-invisible" for="edit-submitted-dislike-feedback">Feedback <span class="form-required" title="This field is required.">*</span></label>
 <div class="form-textarea-wrapper resizable textarea-processed resizable-textarea"><textarea required="required" placeholder="Enter your message..." class="form__control form__control--textarea form-textarea required" id="edit-submitted-dislike-feedback" name="submitted[dislike_feedback]" cols="60" rows="5"></textarea><div class="grippie"></div></div>
</div>
</div></div></div><input type="hidden" name="details[sid]"><input type="hidden" name="details[page_num]" value="1"><input type="hidden" name="details[page_count]" value="1"><input type="hidden" name="details[finished]" value="0"><input type="hidden" name="form_build_id" value="form-2Xudgd1tgAqSODZd-LPCLQw94h2dHoHIvCsJGyZLu_g"><input type="hidden" name="form_id" value="webform_client_form_1680"><input type="hidden" name="honeypot_time" value="1648194723|MVdbX3WEpck_aKvBgU9NfN6KuH-JRLNjspfnhW6uVMk"><div class="phone-textfield"><div class="form-item form-type-textfield form-item-phone">
  <label for="edit-phone">Leave this field blank </label>
 <input autocomplete="off" type="text" id="edit-phone" name="phone" value="" size="20" maxlength="128" class="form-text"></div>
</div><div class="form-actions"><div><div class="d-flex justify-content-end"><input class="webform-submit button-primary btn btn-submit-feedback btn--medium btn--block-sp form-submit ajax-processed" type="submit" id="edit-submit" name="op" value="Submit Feedback"></div></div></div></div></form>    </div>
</section><style>
    #div-gpt-ad-Programizcom36790 {display:none; }
    #div-gpt-ad-Programizcom36794 {display: block; }
    @media(min-width: 992px) { #div-gpt-ad-Programizcom36790 {display: block;} #div-gpt-ad-Programizcom36794 {display: none; }}
    </style><div class="pgAdWrapper" style="min-width: 728px; min-height: 90px; display: flex; justify-content: center; align-items: center;"><div id="div-gpt-ad-Programizcom36790" style=" margin: 48px 0 36px; height: 90px; width: 728px;">
    <div></div></div><div class="adSpinner" style="width: 60px; height: 60px; text-align: center; line-height: 60px; margin: 10px auto; font-size: 12px; position: absolute; display: none;"><span style="color: rgb(243, 243, 243);">Ad</span></div></div>
    
    <div id="div-gpt-ad-Programizcom36794" style="margin: 48px 0 36px; min-height: 250px;">
    </div>
                  </div>
            
          </div>
