import sys

FILENAME_IN  = 'x5.bin'
FILENAME_OUT = 'hack.bin'

NEW_VOLUME_5A = 30 # default: 90
NEW_VOLUME_5F = 30 # default: 95

VOLUME_OFFSETS_5A = [
        0x024ce902,
        0x02584042,
        0x0265f5e2,
        0x02714d22,
        0x027c9b32,
        0x028804d2,
        0x029377a2,
        0x02a07582,
        0x02abccc2,
        0x02b71ad2,
        0x02c5dae2,
        0x02d56512,
        0x02e0bc52,
        0x02eed702,
        0x02fa49d2,
        0x0305bca2,
        0x031881b2,
        0x032ab3c2,
        0x03362692,
        ]

VOLUME_OFFSETS_5F = [
        0x003ad5f6,
        0x004beb36,
        0x005b1056,
        0x006b36b6,
        0x007b8b06,
        0x008b5eb6,
        0x017388a6,
        0x01789816,
        0x0191ae26,
        0x019bfaf6,
        0x01a68816,
        ]


def change_volume(iso, offset, value):
    # left channel
    iso[offset+0x00] = value
    # right channel
    iso[offset+0x20] = value


def change_all_volumes(iso, offsets, value):
    for offset in offsets:
        change_volume(iso, offset, value)


def main():
    with open(FILENAME_IN, 'rb') as inf:
        iso = bytearray(inf.read())

    try:
        volume1 = volume2 = int(sys.argv[1])
    except (IndexError, ValueError):
        volume1 = NEW_VOLUME_5A
        volume2 = NEW_VOLUME_5F

    change_all_volumes(iso, VOLUME_OFFSETS_5A, volume1)
    change_all_volumes(iso, VOLUME_OFFSETS_5F, volume2)

    with open(FILENAME_OUT, 'wb') as outf:
        outf.write(iso)


if __name__ == '__main__':
    main()
