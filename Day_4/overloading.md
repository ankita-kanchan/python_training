<table border="0"><tbody><tr><th>Operator</th>
				<th>Expression</th>
				<th>Internally</th>
			</tr><tr><td>Addition</td>
				<td><code>p1 + p2</code></td>
				<td><code>p1.__add__(p2)</code></td>
			</tr><tr><td>Subtraction</td>
				<td><code>p1 - p2</code></td>
				<td><code>p1.__sub__(p2)</code></td>
			</tr><tr><td>Multiplication</td>
				<td><code>p1 * p2</code></td>
				<td><code>p1.__mul__(p2)</code></td>
			</tr><tr><td>Power</td>
				<td><code>p1 ** p2</code></td>
				<td><code>p1.__pow__(p2)</code></td>
			</tr><tr><td>Division</td>
				<td><code>p1 / p2</code></td>
				<td><code>p1.__truediv__(p2)</code></td>
			</tr><tr><td>Floor Division</td>
				<td><code>p1 // p2</code></td>
				<td><code>p1.__floordiv__(p2)</code></td>
			</tr><tr><td>Remainder (modulo)</td>
				<td><code>p1 % p2</code></td>
				<td><code>p1.__mod__(p2)</code></td>
			</tr><tr><td>Bitwise Left Shift</td>
				<td><code>p1 &lt;&lt; p2</code></td>
				<td><code>p1.__lshift__(p2)</code></td>
			</tr><tr><td>Bitwise Right Shift</td>
				<td><code>p1 &gt;&gt; p2</code></td>
				<td><code>p1.__rshift__(p2)</code></td>
			</tr><tr><td>Bitwise AND</td>
				<td><code>p1 &amp; p2</code></td>
				<td><code>p1.__and__(p2)</code></td>
			</tr><tr><td>Bitwise OR</td>
				<td><code>p1 | p2</code></td>
				<td><code>p1.__or__(p2)</code></td>
			</tr><tr><td>Bitwise XOR</td>
				<td><code>p1 ^ p2</code></td>
				<td><code>p1.__xor__(p2)</code></td>
			</tr><tr><td>Bitwise NOT</td>
				<td><code>~p1</code></td>
				<td><code>p1.__invert__()</code></td>
			</tr></tbody></table>
