<table class="legend">

    <thead>
        <tr><th colspan=2>Legend</th></tr>
        <tr><th>Test</th><th>Purpose</th></tr>
    </thead>
    <tbody>

        <tr>
            <td class="header">T1</td>
            <td class="binarymatrix">
                <div class="title">Binary Matrix Rank Test</div>

<div class="focus">Focus:</div><p>
 test is the rank of disjoint sub-matrices of the entire sequence. 

</p><div class="purpose">Purpose:</div><p> 
 check for linear dependence among fixed 
 length substrings of the original sequence.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence 
 is non-random. Otherwise, conclude that the sequence is random.


            </p></td>
        </tr>
        <tr>
            <td class="header">T2</td>
            <td class="blockfreq">
                <div class="title">Block Frequency Test</div>

<div class="focus">Focus:</div><p>
 test the proportion of zeroes and ones within M-bit blocks. 

</p><div class="purpose">Purpose:</div><p>
  determine whether the frequency of ones is an M-bit block is approximately M/2

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence is non-random. 
 Otherwise, conclude that the sequence is random.

            </p></td>
        </tr>
        <tr>
            <td class="header">T3</td>
            <td class="cumsums">
                <div class="title">Cumulative Sums Test</div>

<div class="focus">Focus:</div><p>
 test the maximal excursion (from zero) of the random walk 
 defined by the cumulative sum of adjusted (-1, +1) digits 
 in the sequence.

</p><div class="purpose">Purpose:</div><p>
 determine whether the cumulative sum of the partial sequences 
 occurring in the tested sequence is too large or too small 
 relative to the expected behavior of that cumulative sum for 
 random sequences.  This cumulative sum may be considered as a 
 random walk. For a random sequence, the random walk should be 
 near zero. For non-random sequences, the excursions of this random 
 walk away from zero will be too large.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence 
 is non-random. Otherwise, conclude that the sequence is random.


            </p></td>
        </tr>
        <tr>
            <td class="header">T4</td>
            <td class="longestrun">
                <div class="title">Longest Run of Ones Test</div>

<div class="focus">Focus:</div><p>
 test the longest run of ones within M-bit blocks.

</p><div class="purpose">Purpose:</div><p>
 determine whether the length of the longest run of ones 
 within the tested sequence is consistent with the length 
 of the longest run of ones that would be expected in a 
 random sequence. Note that an irregularity in the expected 
 length of the longest run of ones implies that there is also 
 an irregularity in the expected length of the longest run of 
 zeroes. Long runs of zeroes were not evaluated separately due 
 to a concern about statistical independence among the tests.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the 
 sequence is non-random. Otherwise, conclude that the sequence 
 is random.


            </p></td>
        </tr>
        <tr>
            <td class="header">T5</td>
            <td class="maurers">
                <div class="title">Maurer's Universal Statistic Test</div>

<div class="focus">Focus:</div><p>
  test the number of bits between matching patterns.

</p><div class="purpose">Purpose:</div><p>
 detect whether or not the sequence can be significantly compressed 
 without loss of information. An overly compressible sequence is 
 considered to be non-random.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence 
 is non-random. Otherwise, conclude that the sequence is random.

            </p></td>
        </tr>
        <tr>
            <td class="header">T6</td>
            <td class="monobitfreq">
                <div class="title">Monobit Frequency Test</div>

<div class="focus">Focus:</div><p> 
 test the proportion of zeroes and ones for the entire sequence. 

</p><div class="purpose">Purpose:</div><p> 
 determine whether that number of ones and zeros in a sequence 
 are approximately the same as would be expected for a truly 
 random sequence. 

</p><div class="outcome">Outcome:</div><p>
 The test assesses the closeness of the fraction of ones to 1/2, 
 that is, the number of ones and zeroes in a sequence should be about the same.

 If the computed P-value is < 0.01, then conclude that the sequence is non-random. 
 Otherwise, conclude that the sequence is random. 

            </p></td>
        </tr>
        <tr>
            <td class="header">T7</td>
            <td class="nonoverlapping">
                <div class="title">Nonoverlapping Template Matching Test</div>

<div class="focus">Focus:</div><p>
 test the number of occurrences of pre-defined target substrings. 

</p><div class="purpose">Purpose:</div><p> 
 reject sequences that exhibit too many occurrences of a given 
 non-periodic (aperiodic) pattern. For this test and for the 
 Overlapping Template Matching test, an m-bit window is used to 
 search for a specific m-bit pattern. If the pattern is not found, 
 the window slides one bit position. For this test, when the pattern 
 is found, the window is reset to the bit after the found pattern,
  and the search resumes.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence is 
 non-random. Otherwise, conclude that the sequence is random.


            </p></td>
        </tr>
        <tr>
            <td class="header">T8</td>
            <td class="overlapping">
                <div class="title">Overlapping Template Matching Test</div>

<div class="focus">Focus:</div><p>
  test the number of pre-defined target substrings.

</p><div class="purpose">Purpose:</div><p> 
 to reject sequences that show deviations from the expected number of 
 runs of ones of a given length. Note that when there is a deviation 
 from the expected number of ones of a given length, there is also a 
 deviation in the runs of zeroes. Runs of zeroes were not evaluated 
 separately due to a concern about statistical independence among the 
 tests. For this test and for the Non-overlapping Template Matching 
 test, an m-bit window is used to search for a specific m-bit pattern. 
 If the pattern is not found, the window slides one bit position. For 
 this test, when the pattern is found, the window again slides one bit, 
 and the search is resumed.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence is 
 non-random. Otherwise, conclude that the sequence is random.


            </p></td>
        </tr>
        <tr>
            <td class="header">T9</td>
            <td class="randomexcursions">
                <div class="title">Random Excursions Test</div>

<div class="focus">Focus:</div><p>
 test the number of cycles having exactly K visits in a cumulative 
 sum random walk. The cumulative sum random walk is found if partial 
 sums of the (0,1) sequence are adjusted to (-1, +1). A random 
 excursion of a random walk consists of a sequence of n steps of unit 
 length taken at random that begin at and return to the origin.

</p><div class="purpose">Purpose:</div><p>
 determine if the number of visits to a state within a random walk 
 exceeds what one would expect for a random sequence.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence is 
 non-random. Otherwise, conclude that the sequence is random.


            </p></td>
        </tr>
        <tr>
            <td class="header">T10</td>
            <td class="randomexcursionsvariant">
                <div class="title">Random Excursions Variant Test</div>

<div class="focus">Focus:</div><p>
 test the number of times that a particular state occurs in a 
 cumulative sum random walk.

</p><div class="purpose">Purpose:</div><p> 
 of this test is to detect deviations from the expected number 
 of occurrences of various states in the random walk.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence
 is non-random. Otherwise, conclude that the sequence is random.

            </p></td>
        </tr>
        <tr>
            <td class="header">T11</td>
            <td class="runs">
                <div class="title">Runs Test</div>

<div class="focus">Focus:</div><p>
 test the total number of zero and one runs in the entire sequence, 
 where a run is an uninterrupted sequence of identical bits. 
 A run of length k means that a run consists of exactly k identical 
 bits and is bounded before and after with a bit of the opposite value. 

</p><div class="purpose">Purpose:</div><p> 
 determine whether the number of runs of ones and zeros of various 
 lengths is as expected for a random sequence. In particular, this 
 test determines whether the oscillation between such substrings is 
 too fast or too slow.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence 
 is non-random. Otherwise, conclude that the sequence is random.

            </p></td>
        </tr>
        <tr>
            <td class="header">T12</td>
            <td class="spectral">
                <div class="title">Spectral Test (Fourier Transform)</div>

<div class="focus">Focus:</div><p>
 test the peak heights in the discrete Fast Fourier Transform. 

</p><div class="purpose">Purpose:</div><p>
 detect periodic features (i.e., repetitive patterns that 
 are near each other) in the tested sequence that would indicate 
 a deviation from the assumption of randomness.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence is 
 non-random. Otherwise, conclude that the sequence is random.

            </p></td>
        </tr>
        <tr>
            <td class="header">T13</td>
            <td class="linearcomplexity">
                <div class="title">Linear Complexity Test</div>

<div class="focus">Focus:</div><p>
 test the length of a generating feedback register.

</p><div class="purpose">Purpose:</div><p>
 determine whether or not the sequence is complex enough to 
 be considered random. Random sequences are characterized by a longer 
 feedback register. A short feedback register implies non-randomness.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence 
 is non-random. Otherwise, conclude that the sequence is random.

            </p></td>
        </tr>

        <tr>
            <td class="header">T14</td>
            <td class="approximateentropy">
                <div class="title">Approximate Entropy Test</div>

<div class="focus">Focus:</div><p>
 test the frequency of each and every overlapping m-bit pattern. 

</p><div class="purpose">Purpose:</div><p>
 compare the frequency of overlapping blocks of two 
 consecutive/adjacent lengths (m and m+1) against the expected 
 result for a random sequence.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence 
 is non-random. Otherwise, conclude that the sequence is random.


            </p></td>
        </tr>

        <tr>
            <td class="header">T15</td>
            <td class="serial">
                <div class="title">Serial Test</div>

<div class="focus">Focus:</div><p>
 test the frequency of each and every overlapping m-bit pattern 
 across the entire sequence.

</p><div class="purpose">Purpose:</div><p>
 determine whether the number of occurrences of the 2m m-bit 
 overlapping patterns is approximately the same as would be 
 expected for a random sequence. The pattern can overlap.

</p><div class="outcome">Outcome:</div><p>
 If the computed P-value is < 0.01, then conclude that the sequence 
 is non-random. Otherwise, conclude that the sequence is random.

            </p></td>
        </tr>
        <tr>
            <td class="header">md5</td>
            <td class="md5">
                <div class="title">md5 sum of the random number</div>
            </p></td>
        </tr>

    </tbody>
</table>

