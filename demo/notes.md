# Personal notes

## Requirements

Check out [this issue](https://github.com/pharmapsychotic/clip-interrogator/issues/62), you may well need:

```bash
pip3 install transformers==4.26.1
```

(And in general, stricter requirements)

## Speed

Slow... around 8s/image for 256x256 pre-loaded in memory.
How to speed up?

* [Issue #19](https://github.com/pharmapsychotic/clip-interrogator/issues/19) suggests `interrogate_fast`. 
    * `interrogate_fast` gets 0.5s locally! (Not as greet, but still decent results)
    * `interrogate_classic` gets 0.5s locally (Similat to _fast, but slightly different output)
    * `interrogate_negative` at 9s (same as interrogate_best) - not sure how useful
* [PR #46](https://github.com/pharmapsychotic/clip-interrogator/pull/46) shows a way to lower memory, swapping out models to RAM when not in use. May be very helpful to quickly swap in, between the stream rendering process.
  * Or maybe just [making sure everything fits in memory](https://stackoverflow.com/questions/65399566/running-two-different-independent-pytorch-programs-on-a-single-gpu)?
