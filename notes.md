

# Summary

The big challenge, undampened zeros.

If you can invert the zeros -> undampend poles in your controller, issues with robustness.
If you invert them, your controller will have a huge reconase at that lokation.

If you chose not to invert those poles, you will have an oscilationory behaviur in your transient respone, see step resonses cl.

If you don't want to invert the zeros, you face the same restrection as if the zeros would have been unstable, i.e. non-minumum phase.

With Hinf and IMC it is possible to achive higher BW and closed loop response, but at a higher cost in terms of robustness.

Pretty hard to beat the AST built in the control. The tru improvoent I would try in a real macghine,  would be to dampen the hiuger resonace, that would not only improve robustness without compirimisng the closed loop response.



