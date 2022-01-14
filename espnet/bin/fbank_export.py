from espnet.utils.torch_mfcc.torch_fbank import FBANK
from espnet.utils.io_utils import LoadInputsAndTargets

import configargparse
import torch
import json
import librosa


class ExportHelper(torch.nn.Module):
    def __init__(
        self,
        model
        ):
        super(ExportHelper, self).__init__()
        self.model = model
    def forward(
        self,
        inputs
        ):
        return self.model.forward_export(inputs)

      

def export_model(
    model,
    example_inputs,
    example_outputs,
    export_tag=""
):  
    random_inputs = [x.clone() if x.dtype!=torch.float32 else torch.randn(x.size()).float() for x in example_inputs]
    export_model_helper = ExportHelper(model).eval()
    script_model = torch.jit.trace(export_model_helper, (random_inputs,))
    script_model_output = script_model(example_inputs)
    for (x,y) in zip(example_outputs, script_model_output):
        print('ave diff:', torch.mean(torch.abs(x.float()-y.float())))

    if (len(export_tag)!=0):
        if (not export_tag.endswith('.pt')):
            export_tag = export_tag+'.pt'
        script_model.save(export_tag)




def get_parser():
    """Get default arguments."""
    parser = configargparse.ArgumentParser(
        description="Transcribe text from speech using "
        "a speech recognition model on one CPU or GPU",
        config_file_parser_class=configargparse.YAMLConfigFileParser,
        formatter_class=configargparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("--recog-wav-dir", type=str)
    parser.add_argument("--recog-json", type=str)

 
  






def main(args):
    """Run the main decoding function."""
    parser = get_parser()
    args = parser.parse_args(args)

    with open(args.recog_json, "rb") as f:
        js = json.load(f)["utts"]

    load_inputs_and_targets = LoadInputsAndTargets(
        mode="asr",
        load_output=False,
        sort_in_input_length=False,
        preprocess_conf=None
        preprocess_args={"train": False},
    )

    with torch.no_grad():
        for idx, name in enumerate(js.keys(), 1):
            batch = [(name, js[name])]
            feat = load_inputs_and_targets(batch)
            

            sig = librosa.load(
            librosa.util.example_audio_file(), duration=10.0, offset=30)[0]
            device='cpu'
            sig_th = th.from_numpy(sig)[None, :].float().to(device)
            fft_len = 1024
            win_hop = 256
            win_len = 1024
            window = 'hann'
            n_mel = 128
            center = False
            sr = 22050

            fbank = FBANK(win_len, win_hop, fft_len, sr,  win_type=window,
              top_db=None,
              center=center, n_mel=n_mel).to(device)

            return 


if __name__ == "__main__":
    main(sys.argv[1:])
