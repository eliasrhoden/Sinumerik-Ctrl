

# Summary

The big challenge, undamped zeros.

If you can invert the zeros -> undamped poles in your controller, issues with robustness.
If you invert them, your controller will have a huge resonance at that location.

If you chose not to invert those poles, you will have an oscillatory behavior in your transient response, see step response closed loop.

If you don't want to invert the zeros, you face the same restriction as if the zeros would have been unstable, i.e. non-minimum phase.

With Hinf and IMC it is possible to achieve higher BW and closed loop response, but at a higher cost in terms of robustness.

Pretty hard to beat the AST built in the control. The true improvement I would try in a real machine,  would be to dampen the higher resonance, that would not only improve robustness without compromising the closed loop response.
