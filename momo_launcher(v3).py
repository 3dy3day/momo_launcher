from os import kill
import os
import sys
import subprocess
import tkinter as tk
import tkinter.ttk as ttk

def boot():
    global proc
    command = './momo --video-device ' + video_comb.get() + ' --resolution ' + resolution_comb.get() + \
        ' sora '\
            ' --signaling-url wss://' + endpoint_box.get() + \
            ' --channel-id ' + channel_box.get() + \
            ' --video-codec-type ' + codec_comb.get() + \
            ' --video-bit-rate ' + bit_comb.get() + \
            ' --audio ' + audio_comb.get() + ' --role sendonly'
    print(command)
    # proc = subprocess.Popen("exec " + command, shell=True)

def stop():
    # global proc
    proc.kill()
    print("process stopped")
    return

def main():
    global video_comb, resolution_comb, endpoint_box, channel_box, codec_comb, bit_comb, audio_comb
    # Main Window
    main_win = tk.Tk()
    main_win.title("momo launcher v2")
    # Main Frame
    main_frm = ttk.Frame(main_win)
    main_frm.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)


    # Widget endpoint
    endpoint_label = ttk.Label(main_frm, text="Endpoint")
    endpoint_box = ttk.Entry(main_frm)
    endpoint_box.insert(0, "sora.low-l.com/signaling")
    # Widget channel
    channel_label = ttk.Label(main_frm, text="Channel")
    channel_box = ttk.Entry(main_frm)
    channel_box.insert(0, "test")

    # Widget video device
    video_label = ttk.Label(main_frm, text="Video Device")

    process = subprocess.run(['ls -a /dev/video*'],stdout=subprocess.PIPE, shell=True)
    out = process.stdout.decode()
    if type(out) != "list":
        out = ["OBS"]
    video_comb = ttk.Combobox(main_frm, values=out, width=10)
    video_comb.current(0)

    # Widget resolution
    resolution_label = ttk.Label(main_frm, text="Resolution")
    resolution_comb = ttk.Combobox(
        main_frm, values=['QVGA', 'VGA', 'HD', 'FHD', '4K'], width=10)
    resolution_comb.current(4)

    #Widget framerate
    framerate_label = ttk.Label(main_frm, text="Framerate")
    framerate_comb = ttk.Combobox(main_frm, values=['10', '20', '30', '40', '50', '60'], width=10)
    framerate_comb.current(2)

    # Widget audio device
    audio_label = ttk.Label(main_frm, text="Audio")
    audio_comb = ttk.Combobox(main_frm, values=['false', 'true'], width=10)
    audio_comb.current(0)

    # Widget video codec type
    codec_label = ttk.Label(main_frm, text="Video Codec Type")
    codec_comb = ttk.Combobox(
        main_frm, values=['AV1', 'H264', 'VP8', 'VP9'], width=10)
    codec_comb.current(1)

    # Widget video bit rate
    bit_label = ttk.Label(main_frm, text="Video Bit Rate")
    bitrate = list(range(3000, 30001, 3000))
    bit_comb = ttk.Combobox(main_frm, values=bitrate, width=10)
    bit_comb.current(2)

    # Widget start button
    app_btn = ttk.Button(main_frm, text="Start", command=boot)

    # Widget stop button
    stp_btn = ttk.Button(main_frm, text="Stop", command=stop)

    # Arrange Widgets
    endpoint_label.grid(column=0, row=0, pady=10)
    endpoint_box.grid(column=1, row=0, sticky=tk.EW, pady=5)

    channel_label.grid(column=0, row=1)
    channel_box.grid(column=1, row=1, sticky=tk.EW, pady=5)

    video_label.grid(column=0, row=2)
    video_comb.grid(column=1, row=2, pady=5, padx=5, ipadx=5)

    resolution_label.grid(column=0, row=4)
    resolution_comb.grid(column=1, row=4, pady=5, padx=5, ipadx=5)

    framerate_label.grid(column=2, row=4)
    framerate_comb.grid(column=3, row=4, pady=5, padx=5, ipadx=5)

    audio_label.grid(column=2, row=2)
    audio_comb.grid(column=3, row=2, pady=5, padx=5, ipadx=5)

    codec_label.grid(column=0, row=3)
    codec_comb.grid(column=1, row=3, pady=5, padx=5, ipadx=5)

    bit_label.grid(column=2, row=3)
    bit_comb.grid(column=3, row=3, pady=5, padx=5, ipadx=5)

    app_btn.grid(column=1, row=5, pady=10)
    stp_btn.grid(column=2, row=5, pady=10)

    # Arrange Settings
    main_win.columnconfigure(0, weight=1)
    main_win.rowconfigure(0, weight=1)
    main_frm.columnconfigure(1, weight=1)

    main_frm.mainloop()

if __name__ == "__main__":
    main()