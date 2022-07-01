import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1402_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1402_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1402.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T1402._SN', 'ED6_DT21/T1402_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7CD3
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_A1(0x0017, 0x0003)
    OP_A1(0x0018, 0x0004)
    OP_A1(0x0019, 0x0005)
    OP_A1(0x001A, 0x0006)
    OP_A1(0x001B, 0x0007)
    OP_A1(0x001C, 0x0008)
    OP_A1(0x001D, 0x0009)
    OP_A1(0x001E, 0x000A)
    OP_A1(0x001F, 0x000B)
    OP_A1(0x0020, 0x000C)
    OP_A1(0x0021, 0x000D)
    OP_A1(0x0022, 0x000E)
    OP_A1(0x0023, 0x000F)
    OP_A1(0x0024, 0x0010)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x000A, 0x0020)
    OP_72(0x000B, 0x0020)
    OP_72(0x000C, 0x0020)
    OP_72(0x000D, 0x0020)
    OP_72(0x000E, 0x0020)
    OP_72(0x000F, 0x0020)
    OP_72(0x0010, 0x0020)
    OP_D2(0x00070020, 0x00070028, 0x00)
    OP_D2(0x00070050, 0x00070058, 0x01)
    OP_D2(0x00070060, 0x00070068, 0x02)
    OP_D2(0x00070070, 0x00070078, 0x03)
    OP_D2(0x00270398, 0x0027039C, 0x04)
    OP_D2(0x002701E7, 0x002701EC, 0x05)
    OP_D2(0x002701EE, 0x002701F3, 0x06)
    OP_D2(0x00070150, 0x00070154, 0x07)
    OP_D2(0x002701D2, 0x002701D7, 0x08)
    OP_D2(0x00270202, 0x00270207, 0x09)
    OP_D2(0x00070120, 0x00070124, 0x0A)
    OP_D2(0x002701E6, 0x002701EB, 0x0B)
    OP_D2(0x00060108, 0x0006010D, 0x0C)
    OP_D2(0x002701D3, 0x002701D8, 0x0D)
    OP_D2(0x00070142, 0x00070146, 0x0E)
    OP_D2(0x00270080, 0x00270084, 0x0F)
    OP_D2(0x0026023D, 0x00260242, 0x10)
    OP_D2(0x00270399, 0x0027039D, 0x11)
    OP_D2(0x00070021, 0x00070029, 0x12)
    OP_D2(0x00070051, 0x00070059, 0x13)
    OP_D2(0x00070061, 0x00070069, 0x14)
    OP_D2(0x00070071, 0x00070079, 0x15)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 560)
    SetChrChipByIndex(0x0008, 0)
    SetChrChipByIndex(0x0009, 1)
    SetChrChipByIndex(0x000A, 2)
    SetChrChipByIndex(0x000B, 3)
    SetChrChipByIndex(0x000C, 4)
    SetChrChipByIndex(0x000D, 5)
    SetChrChipByIndex(0x000E, 6)
    SetChrChipByIndex(0x000F, 7)
    SetChrChipByIndex(0x0010, 8)
    SetChrChipByIndex(0x0027, 9)
    SetChrChipByIndex(0x0028, 9)
    SetChrChipByIndex(0x0029, 9)
    SetChrChipByIndex(0x002A, 9)
    SetChrChipByIndex(0x002B, 9)
    SetChrChipByIndex(0x002C, 9)
    SetChrChipByIndex(0x002D, 9)
    SetChrChipByIndex(0x002E, 9)
    SetChrChipByIndex(0x002F, 9)
    SetChrChipByIndex(0x0030, 9)
    SetChrChipByIndex(0x0031, 9)
    SetChrChipByIndex(0x0032, 9)
    SetChrChipByIndex(0x0033, 9)
    SetChrChipByIndex(0x0034, 9)
    SetChrChipByIndex(0x0035, 9)
    SetChrChipByIndex(0x0036, 9)
    SetChrChipByIndex(0x0037, 9)
    SetChrChipByIndex(0x0038, 9)
    SetChrChipByIndex(0x0039, 9)
    SetChrChipByIndex(0x003A, 9)
    SetChrChipByIndex(0x003B, 9)
    SetChrChipByIndex(0x003C, 9)
    SetChrChipByIndex(0x003D, 9)
    SetChrChipByIndex(0x003E, 9)
    SetChrChipByIndex(0x003F, 9)
    SetChrChipByIndex(0x0040, 9)
    SetChrChipByIndex(0x0041, 9)
    SetChrChipByIndex(0x0042, 9)
    SetChrChipByIndex(0x0043, 9)
    SetChrChipByIndex(0x0044, 9)
    SetChrChipByIndex(0x0045, 9)
    SetChrChipByIndex(0x0046, 9)
    SetChrChipByIndex(0x0047, 9)
    SetChrChipByIndex(0x0048, 9)
    SetChrChipByIndex(0x0049, 9)
    SetChrChipByIndex(0x004A, 9)
    SetChrChipByIndex(0x004B, 9)
    SetChrChipByIndex(0x004C, 9)
    SetChrChipByIndex(0x004D, 9)
    SetChrChipByIndex(0x004E, 9)
    SetChrChipByIndex(0x004F, 9)
    SetChrChipByIndex(0x0050, 9)
    SetChrChipByIndex(0x0051, 9)
    SetChrChipByIndex(0x0052, 9)
    SetChrChipByIndex(0x0053, 9)
    SetChrChipByIndex(0x0054, 9)
    SetChrChipByIndex(0x0055, 9)
    SetChrChipByIndex(0x0056, 9)
    SetChrChipByIndex(0x0057, 9)
    SetChrChipByIndex(0x0058, 9)
    SetChrChipByIndex(0x0059, 9)
    SetChrChipByIndex(0x005A, 9)
    SetChrChipByIndex(0x005B, 9)
    SetChrChipByIndex(0x005C, 9)
    SetChrChipByIndex(0x005D, 9)
    SetChrChipByIndex(0x005E, 9)
    SetChrChipByIndex(0x005F, 9)
    SetChrChipByIndex(0x0060, 9)
    SetChrChipByIndex(0x0061, 9)
    SetChrChipByIndex(0x0062, 9)
    SetChrChipByIndex(0x0063, 9)
    SetChrChipByIndex(0x0064, 9)
    SetChrChipByIndex(0x0065, 9)
    SetChrChipByIndex(0x0066, 9)
    SetChrChipByIndex(0x0067, 9)
    SetChrChipByIndex(0x0068, 9)
    SetChrChipByIndex(0x0069, 9)
    SetChrChipByIndex(0x006A, 9)
    SetChrChipByIndex(0x006B, 9)
    SetChrChipByIndex(0x006C, 9)
    SetChrChipByIndex(0x006D, 9)
    SetChrChipByIndex(0x006E, 9)
    SetChrChipByIndex(0x006F, 9)
    SetChrChipByIndex(0x0070, 9)
    SetChrChipByIndex(0x0071, 9)
    SetChrChipByIndex(0x0072, 9)
    SetChrChipByIndex(0x0073, 9)
    SetChrChipByIndex(0x0074, 9)
    SetChrChipByIndex(0x0075, 9)
    SetChrChipByIndex(0x0076, 9)
    SetChrChipByIndex(0x0077, 9)
    SetChrChipByIndex(0x0078, 9)
    SetChrChipByIndex(0x0079, 9)
    SetChrChipByIndex(0x007A, 9)
    SetChrChipByIndex(0x007B, 9)
    SetChrChipByIndex(0x007C, 9)
    SetChrChipByIndex(0x007D, 9)
    SetChrChipByIndex(0x007E, 9)
    SetChrChipByIndex(0x0015, 10)
    SetChrChipByIndex(0x0016, 10)
    SetChrChipByIndex(0x0011, 11)
    SetChrPos(0x0017, -7460, 0, 104890, 0)
    SetChrPos(0x0018, 3360, 0, 104630, 0)
    SetChrPos(0x0019, -7650, 0, 119070, 0)
    SetChrPos(0x001A, 3510, 0, 119050, 0)
    SetChrPos(0x001B, -18530, 0, 108310, 0)
    SetChrPos(0x001C, 15560, 0, 109270, 0)
    SetChrPos(0x001D, -19230, 0, 123310, 0)
    SetChrPos(0x001E, 14300, 0, 123350, 0)
    SetChrPos(0x001F, -8090, 0, 133010, 0)
    SetChrPos(0x0020, 3690, 0, 132830, 0)
    SetChrPos(0x0021, 2670, 0, 149120, 0)
    SetChrPos(0x0022, -8410, 0, 149060, 0)
    SetChrPos(0x0023, -19940, 0, 140900, 0)
    SetChrPos(0x0024, 12450, 0, 140010, 0)
    SetChrPos(0x0027, -7630, 0, 157450, 180)
    SetChrPos(0x0028, -5660, -50, 157450, 180)
    SetChrPos(0x0029, -3630, 0, 157450, 180)
    SetChrPos(0x002A, -1730, 90, 157450, 180)
    SetChrPos(0x002B, 230, -30, 157450, 180)
    SetChrPos(0x002C, 2070, -30, 157450, 180)
    SetChrPos(0x002D, -7630, 40, 159600, 180)
    SetChrPos(0x002E, -5660, 20, 159600, 180)
    SetChrPos(0x002F, -3630, -20, 159600, 180)
    SetChrPos(0x0030, -1730, 50, 159600, 180)
    SetChrPos(0x0031, 230, -20, 159600, 180)
    SetChrPos(0x0032, 2070, -50, 159600, 180)
    SetChrPos(0x0033, -7630, 30, 161750, 180)
    SetChrPos(0x0034, -5660, 10, 161750, 180)
    SetChrPos(0x0035, -3630, 20, 161750, 180)
    SetChrPos(0x0036, -1730, 70, 161750, 180)
    SetChrPos(0x0037, 230, -10, 161750, 180)
    SetChrPos(0x0038, 2070, -30, 161750, 180)
    SetChrPos(0x0039, -7630, -20, 163900, 180)
    SetChrPos(0x003A, -5660, -40, 163900, 180)
    SetChrPos(0x003B, -3630, -40, 163900, 180)
    SetChrPos(0x003C, -1730, 40, 163900, 180)
    SetChrPos(0x003D, 230, -40, 163900, 180)
    SetChrPos(0x003E, 2070, -20, 163900, 180)
    SetChrPos(0x003F, -7630, -40, 166050, 180)
    SetChrPos(0x0040, -5660, 0, 166050, 180)
    SetChrPos(0x0041, -3630, 30, 166050, 180)
    SetChrPos(0x0042, -1730, 60, 166050, 180)
    SetChrPos(0x0043, 230, 10, 166050, 180)
    SetChrPos(0x0044, 2070, -20, 166050, 180)
    ClearChrFlags(0x0027, 0x0080)
    ClearChrFlags(0x0028, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    ClearChrFlags(0x002D, 0x0080)
    ClearChrFlags(0x002E, 0x0080)
    ClearChrFlags(0x002F, 0x0080)
    ClearChrFlags(0x0030, 0x0080)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0033, 0x0080)
    ClearChrFlags(0x0034, 0x0080)
    ClearChrFlags(0x0035, 0x0080)
    ClearChrFlags(0x0036, 0x0080)
    ClearChrFlags(0x0037, 0x0080)
    ClearChrFlags(0x0038, 0x0080)
    ClearChrFlags(0x0039, 0x0080)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    ClearChrFlags(0x003E, 0x0080)
    ClearChrFlags(0x003F, 0x0080)
    ClearChrFlags(0x0040, 0x0080)
    ClearChrFlags(0x0041, 0x0080)
    ClearChrFlags(0x0042, 0x0080)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    SetChrFlags(0x0027, 0x0200)
    SetChrFlags(0x0028, 0x0200)
    SetChrFlags(0x0029, 0x0200)
    SetChrFlags(0x002A, 0x0200)
    SetChrFlags(0x002B, 0x0200)
    SetChrFlags(0x002C, 0x0200)
    SetChrFlags(0x002D, 0x0200)
    SetChrFlags(0x002E, 0x0200)
    SetChrFlags(0x002F, 0x0200)
    SetChrFlags(0x0030, 0x0200)
    SetChrFlags(0x0031, 0x0200)
    SetChrFlags(0x0032, 0x0200)
    SetChrFlags(0x0033, 0x0200)
    SetChrFlags(0x0034, 0x0200)
    SetChrFlags(0x0035, 0x0200)
    SetChrFlags(0x0036, 0x0200)
    SetChrFlags(0x0037, 0x0200)
    SetChrFlags(0x0038, 0x0200)
    SetChrFlags(0x0039, 0x0200)
    SetChrFlags(0x003A, 0x0200)
    SetChrFlags(0x003B, 0x0200)
    SetChrFlags(0x003C, 0x0200)
    SetChrFlags(0x003D, 0x0200)
    SetChrFlags(0x003E, 0x0200)
    SetChrFlags(0x003F, 0x0200)
    SetChrFlags(0x0040, 0x0200)
    SetChrFlags(0x0041, 0x0200)
    SetChrFlags(0x0042, 0x0200)
    SetChrFlags(0x0043, 0x0200)
    SetChrFlags(0x0044, 0x0200)
    SetChrFlags(0x0045, 0x0200)
    SetChrFlags(0x0046, 0x0200)
    SetChrFlags(0x0047, 0x0200)
    SetChrFlags(0x0048, 0x0200)
    SetChrFlags(0x0049, 0x0200)
    SetChrFlags(0x004A, 0x0200)
    SetChrFlags(0x004B, 0x0200)
    SetChrFlags(0x004C, 0x0200)
    SetChrFlags(0x004D, 0x0200)
    SetChrFlags(0x004E, 0x0200)
    SetChrFlags(0x004F, 0x0200)
    SetChrFlags(0x0050, 0x0200)
    SetChrFlags(0x0051, 0x0200)
    SetChrFlags(0x0052, 0x0200)
    SetChrFlags(0x0053, 0x0200)
    SetChrFlags(0x0054, 0x0200)
    SetChrFlags(0x0055, 0x0200)
    SetChrFlags(0x0056, 0x0200)
    SetChrFlags(0x0057, 0x0200)
    SetChrFlags(0x0058, 0x0200)
    SetChrFlags(0x0059, 0x0200)
    SetChrFlags(0x005A, 0x0200)
    SetChrFlags(0x005B, 0x0200)
    SetChrFlags(0x005C, 0x0200)
    SetChrFlags(0x005D, 0x0200)
    SetChrFlags(0x005E, 0x0200)
    SetChrFlags(0x005F, 0x0200)
    SetChrFlags(0x0060, 0x0200)
    SetChrFlags(0x0061, 0x0200)
    SetChrFlags(0x0062, 0x0200)
    SetChrFlags(0x0063, 0x0200)
    SetChrFlags(0x0064, 0x0200)
    SetChrFlags(0x0065, 0x0200)
    SetChrFlags(0x0066, 0x0200)
    SetChrFlags(0x0067, 0x0200)
    SetChrFlags(0x0068, 0x0200)
    SetChrFlags(0x0069, 0x0200)
    SetChrFlags(0x006A, 0x0200)
    SetChrFlags(0x006B, 0x0200)
    SetChrFlags(0x006C, 0x0200)
    SetChrFlags(0x006D, 0x0200)
    SetChrFlags(0x006E, 0x0200)
    SetChrFlags(0x006F, 0x0200)
    SetChrFlags(0x0070, 0x0200)
    SetChrFlags(0x0071, 0x0200)
    SetChrFlags(0x0072, 0x0200)
    SetChrFlags(0x0073, 0x0200)
    SetChrFlags(0x0074, 0x0200)
    SetChrFlags(0x0075, 0x0200)
    SetChrFlags(0x0076, 0x0200)
    SetChrFlags(0x0077, 0x0200)
    SetChrFlags(0x0078, 0x0200)
    SetChrFlags(0x0079, 0x0200)
    SetChrFlags(0x007A, 0x0200)
    SetChrFlags(0x007B, 0x0200)
    SetChrFlags(0x007C, 0x0200)
    SetChrFlags(0x007D, 0x0200)
    SetChrFlags(0x007E, 0x0200)
    SetChrPos(0x0015, 1600, -20, 50600, 315)
    SetChrPos(0x0016, -3370, 30, 50630, 315)
    SetChrPos(0x000F, -1440, 40, 53120, 315)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x0101, -2540, 40, 55190, 270)
    SetChrPos(0x0102, 360, 80, 47660, 315)
    SetChrPos(0x0008, -1530, 20, 46400, 315)
    SetChrPos(0x0009, 1350, 50, 45360, 315)
    SetChrPos(0x000B, 0, 80, 44800, 315)
    SetChrPos(0x000A, 610, -30, 46380, 315)
    SetChrPos(0x000C, -810, 10, 55140, 270)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000E, -3380, -40, 95890, 270)
    SetChrPos(0x000D, -1930, 50, 94710, 270)
    SetChrPos(0x0010, -1500, 20, 97080, 270)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0027, -3900, 20, 98320, 270)
    SetChrPos(0x0028, 40, 10, 98140, 270)
    ClearChrFlags(0x0027, 0x0080)
    ClearChrFlags(0x0028, 0x0080)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 330)
    OP_70(0x0002, 0x000001AE)
    OP_A1(0x0025, 0x0002)
    SetChrPos(0x0025, -38270, 26200, 57080, 30)
    OP_A1(0x0026, 0x0011)
    SetChrPos(0x0026, -38270, 5000, 57080, 30)
    OP_75(0x11, 0x00000000, 0x00)
    OP_74(0x0011, 0x00000000, 0x0007)
    LoadEffect(0x00, 'map\\mp021_00.eff')
    LoadEffect(0x01, 'map\\onsen00.eff')
    Yield()
    OP_89(0x0011, -29500, 28800, 67950, 90)
    SetChrFlags(0x0011, 0x0004)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0020)
    SetChrFlags(0x0011, 0x0040)
    SetChrBattleFlags(0x0011, 0x0020)
    Yield()
    ClearChrFlags(0x0011, 0x0004)
    OP_22(0x0125, 0x01, 0x50)
    ClearMapFlags(0x00100000)
    OP_6D(-36460, 10220, 60860, 0)
    OP_67(0, 15110, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(132000, 0)
    OP_6E(500, 0)
    FadeIn(1000, 0)
    CreateThread(0x0025, 0x00, 0x01, 0x0004)
    CreateThread(0x0026, 0x00, 0x01, 0x0005)

    @scena.Lambda('lambda_0BC0')
    def lambda_0BC0():
        OP_6D(-35940, -30, 58750, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BC0)

    @scena.Lambda('lambda_0BD8')
    def lambda_0BD8():
        OP_67(0, 6930, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0BD8)

    @scena.Lambda('lambda_0BF0')
    def lambda_0BF0():
        OP_6B(5550, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0BF0)

    @scena.Lambda('lambda_0C00')
    def lambda_0C00():
        OP_6C(227000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0C00)

    @scena.Lambda('lambda_0C10')
    def lambda_0C10():
        OP_6E(675, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0C10)

    OP_12(0x00009C40, 0x0002A23A, 0x00001388)

    @scena.Lambda('lambda_0C2D')
    def lambda_0C2D():
        OP_8F(0x00FE, -38270, 200, 57080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_0C2D)

    @scena.Lambda('lambda_0C48')
    def lambda_0C48():
        OP_8F(0x00FE, -38270, 5200, 57080, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_0C48)

    @scena.Lambda('lambda_0C63')
    def lambda_0C63():
        OP_8F(0x00FE, -29320, 7600, 68190, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0C63)

    Sleep(1500)

    @scena.Lambda('lambda_0C83')
    def lambda_0C83():
        OP_8F(0x00FE, -38270, 5200, 57080, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_0C83)

    PlayEffect(0x00, 0x00, 0x00FF, -39070, -150, 58410, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00CC, 0x00, 0x64)
    Sleep(2000)

    @scena.Lambda('lambda_0CDD')
    def lambda_0CDD():
        OP_8F(0x00FE, -38270, 5200, 57080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_0CDD)

    WaitForThreadExit(0x0025, 0x0001)
    WaitForThreadExit(0x0025, 0x0000)
    OP_82(0x00, 0x02)
    OP_23(0x00CC)
    OP_23(0x0125)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x00000064)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    Yield()
    OP_89(0x0011, -29320, 7600, 68190, 90)
    ClearChrFlags(0x0011, 0x0004)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0020)
    SetChrFlags(0x0011, 0x0040)
    SetChrBattleFlags(0x0011, 0x0020)
    OP_6D(-29380, 8600, 68010, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(255000, 0)
    OP_6E(474, 0)
    OP_11(0xA0, 0xB4, 0xFF, 0x00009C40, 0x000245C1, 0x00000000)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0011,
        (
            '#0160380879V#1125F#5P这就是此时此刻\n',
            '我们能证明给你们看的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160380880V#1120F请随意观赏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380881V#1008F老爸……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000E, -17920, -260, 72900, 180)
    SetChrPos(0x000D, -17700, -290, 72030, 180)

    ChrTalk(
        0x000E,
        (
            '#0690380882V#883F#5P卡、卡西乌斯·布莱特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160380883V#1120F#5P赛克斯少将，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160380884V#1124F噢～……现在是中将了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380885V#886F#5P少说废话！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380886V#885F为、为什么你会来这里……\n',
            '还有，那艘船是怎么回事！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380887V在这样的状况下\n',
            '怎么还能飞上天空的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160380888V#1125F#5P抱歉，我只能说这是\n',
            '国家机密吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160380889V#1122F就像贵国为何\n',
            '留存有蒸气坦克一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380890V#886F#5P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380891V#892F#5P唔……\n',
            '这就是传说中的『埃尔赛尤』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380892V而您就是那位有名的\n',
            '卡西乌斯·布莱特准将吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160380893V#1125F#5P幸会，殿下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160380894V#1120F虽然感觉似乎\n',
            '曾经在哪里见过面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380895V#894F#5P真是奇遇啊，准将。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380896V#890F我竟然也有\n',
            '同感呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160380897V#1124F#5P那可真是巧啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380898V#894F#5P说得没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#891F#5P哈哈哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0011,
        (
            '#0160380900V#1121F#5P哈哈哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x000E,
        (
            '#0690380901V#885F#5P#4S皇、皇子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(-950, 40, 92660, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(147000, 0)
    OP_6E(495, 0)
    SetChrPos(0x000E, -3380, -40, 95890, 135)
    SetChrPos(0x000D, -1930, 50, 94710, 270)

    @scena.Lambda('lambda_125F')
    def lambda_125F():
        OP_8C(0x00FE, 180, 0)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_125F)

    @scena.Lambda('lambda_126D')
    def lambda_126D():
        OP_8C(0x00FE, 180, 0)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_126D)

    @scena.Lambda('lambda_127B')
    def lambda_127B():
        OP_8C(0x00FE, 180, 0)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_127B)

    OP_8C(0x000D, 180, 0)

    @scena.Lambda('lambda_1290')
    def lambda_1290():
        OP_8C(0x00FE, 180, 0)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1290)

    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0040380902V#890F#5P科洛蒂娅公主、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380903V我是高贵的埃雷波尼亚皇族。\n',
            '之前的约定我会遵守的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380904V我立即命令这附近的\n',
            '帝国军部队全部撤退。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_134A')
    def lambda_134A():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_134A)

    @scena.Lambda('lambda_1358')
    def lambda_1358():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1358)

    ChrTalk(
        0x0101,
        (
            '#0010380905V#1017F#3P奥利维尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380906V#1168F#3P……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380907V#894F#5P不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380908V仅仅展示了可能性，\n',
            '我帝国的国民自然是无法认同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380909V#892F现在就让我亲自\n',
            '乘上埃尔赛尤\n',
            '视察一番如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#0690380910V#883F#6P皇、皇子！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(-940, 0, 52290, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(171000, 0)
    OP_6E(304, 0)
    SetChrPos(0x0015, 1600, -20, 50600, 0)
    SetChrPos(0x0016, -3370, 30, 50630, 0)
    SetChrPos(0x000F, -1440, 40, 53120, 0)
    SetChrPos(0x0101, -2540, 40, 55190, 0)
    SetChrPos(0x0102, -500, 80, 47660, 0)
    SetChrPos(0x0008, -1530, 20, 46400, 0)
    SetChrPos(0x0009, 1350, 50, 45360, 0)
    SetChrPos(0x000B, 0, 80, 44800, 0)
    SetChrPos(0x000A, 610, -30, 46380, 0)
    SetChrPos(0x000C, -810, 10, 55140, 0)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0011, -12350, -70, 82680, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0160380911V#1125F#5P唔、皇子亲自视察的话\n',
            '帝国政府应该就能接受了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160380912V#1120F如何呢，科洛蒂娅殿下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380913V#1167F#5P当然，正合我意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380914V利贝尔与埃雷波尼亚的友情\n',
            '联结也将更加牢固吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380915V#1168F欢迎您。\n',
            '奥利维特皇子殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_6D(-1440, 30, 143110, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(45000, 0)
    OP_6E(488, 0)
    SetChrPos(0x000E, -2070, 40, 143810, 180)
    SetChrPos(0x000D, -2510, 30, 141080, 0)
    SetChrPos(0x0010, -1780, 50, 140180, 0)
    SetChrPos(0x0027, -7630, 0, 157450, 180)
    SetChrPos(0x0028, -5660, -50, 157450, 180)
    SetChrPos(0x0011, -29320, 7500, 68190, 90)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000D, 0)
    SetChrSubChip(0x0010, 0)

    @scena.Lambda('lambda_178B')
    def lambda_178B():
        OP_6B(1700, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_178B)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000E,
        (
            '#0690380916V#885F#5P……皇子！\n',
            '您到底作何打算？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380917V本以为您\n',
            '难得露面，\n',
            '结、结果却演了这么出猴子戏……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380918V#891F#6P哈哈哈。\n',
            '还是被看穿了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380919V#886F#5P当然了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380920V没想到皇子竟\n',
            '在利贝尔谋划着这种事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380921V#885F穆拉！\n',
            '有你跟着，怎么还会发生这种事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0110380922V#272F#4P恕我直言，叔叔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110380923V您认为这个人\n',
            '会乖乖听我的话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380924V#886F#5P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0110380925V#270F#4P而且有些事情，\n',
            '连我也无法接受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110380926V『哈梅尔的悲剧』……\n',
            '由于这次的事件，我才终于知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380927V#883F#5P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0110380928V#276F#4P……您果然知道的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380929V#891F#6P哈哈，老师不可能\n',
            '不知道那件事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380930V#890F当时您已经是\n',
            '军队中的重要人物了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380931V#884F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380932V#891F#6P不过，老师。\n',
            '我并不是在责备您。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380933V那只是一部分主战派\n',
            '的企图，和老师您完全\n',
            '没有关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 270, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0040380934V#894F#2P由于是重大的丑闻，\n',
            '因此进行了彻底的情报管制……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380935V虽然难以赞成，但还是可以理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380936V将污点掩埋，祈祷女神的宽恕，\n',
            '对国民来说，这就是国家的正义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380937V#897F然而……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 0, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0040380938V#896F#6P──我绝不允许\n',
            '相同的欺瞒再发生第二次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380939V#883F#5P…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380940V#897F#6P老师，您其实也\n',
            '应该注意到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380941V过于唐突地出动蒸气坦克……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380942V还有在极其不自然的\n',
            '时机发出的出击命令……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380943V#899F一切都是『铁血宰相』\n',
            '基利亚斯·奥斯本\n',
            '所策划的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380944V#882F#5P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380945V#899F#6P这次的事情让我完全确信了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380946V他一定\n',
            '与『噬身之蛇』有所勾结。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380947V#895F这种事会为帝国\n',
            '带来怎样的影响，\n',
            '我目前还无法断言……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380948V但无论如何，这并不是\n',
            '一国的宰相应有的举止吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380949V#884F#5P………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380950V#882F皇子，难不成您……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380951V#890F#6P呵呵，正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380952V#894F１０年前崭露头角后\n',
            '成为帝国政府的中心人物，\n',
            '军部出身的政治家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380953V在帝国全境铺设铁路网，\n',
            '武力合并数个自治州…\n',
            '冷血而大胆无畏的改革者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380954V#896F我已决心惩治那个\n',
            '蚕食着帝国的怪物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380955V这次的行动\n',
            '就是对他的宣战布告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380956V#884F#5P……既然如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380957V#882F皇子……\n',
            '您能理解\n',
            '这件事的困难程度吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380958V#895F#6P这个当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380959V#893F政府自不必说，连军队也都有七成\n',
            '都在他的控制之下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380960V除了老师这样的中立派，\n',
            '反对势力只剩下开始衰弱的诸侯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380961V而更糟糕的是\n',
            '父亲对其的信赖也相当深厚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380962V#892F真是个怪物一样的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380963V#885F#5P那为何还……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380964V#894F#6P哼，这还用说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380965V#890F因为他的做法太缺乏美感了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380966V#883F#5P！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380967V#891F#6P在利贝尔的旅行\n',
            '让我更加确信，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380968V人和国家，只要有心\n',
            '可以变得无比高贵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380969V#890F而我希望我的祖国和同胞\n',
            '也能拥有同样的高贵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380970V可以的话，希望老师\n',
            '也能协助我的理想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380971V#883F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380972V#884F……皇子。\n',
            '您真是长大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380973V#891F#6P呵呵，\n',
            '士别三日当刮目相看嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380974V#890F更何况，和老师学习武术和兵法\n',
            '已经是７年前的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380975V我也稍微成长了一点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380976V#884F#5P呵呵……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380977V#882F……关于撤退我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380978V但是，我们第３师团\n',
            '只不过是先驱部队而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380979V在帝都，宰相阁下已经\n',
            '陆续集结了１０个师团。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380980V#884F包括今天一共３日……\n',
            '不能再宽限更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380981V#895F#6P啊啊……我明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380982V#881F#5P穆拉。\n',
            '你也跟皇子一起去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380983V要是情况危险的话，\n',
            '就算揪着他的头发也都要把他给我拖回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0110380984V#277F#4P嗯嗯，原本就是这个打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0045, 4000, 0, 157450, 180)
    SetChrPos(0x0046, 5930, -50, 157450, 180)
    SetChrPos(0x0047, 7900, 0, 157450, 180)
    SetChrPos(0x0048, 9800, 90, 157450, 180)
    SetChrPos(0x0049, 11700, -30, 157450, 180)
    SetChrPos(0x004A, 13540, -30, 157450, 180)
    SetChrPos(0x004B, 4000, 40, 159600, 180)
    SetChrPos(0x004C, 5930, 20, 159600, 180)
    SetChrPos(0x004D, 7900, -20, 159600, 180)
    SetChrPos(0x004E, 9800, 50, 159600, 180)
    SetChrPos(0x004F, 11700, -20, 159600, 180)
    SetChrPos(0x0050, 13540, -50, 159600, 180)
    SetChrPos(0x0051, 4000, 30, 161750, 180)
    SetChrPos(0x0052, 5930, 10, 161750, 180)
    SetChrPos(0x0053, 7900, 20, 161750, 180)
    SetChrPos(0x0054, 9800, 70, 161750, 180)
    SetChrPos(0x0055, 11700, -10, 161750, 180)
    SetChrPos(0x0056, 13540, -30, 161750, 180)
    SetChrPos(0x0057, 4000, -20, 163900, 180)
    SetChrPos(0x0058, 5930, -40, 163900, 180)
    SetChrPos(0x0059, 7900, -40, 163900, 180)
    SetChrPos(0x005A, 9800, 40, 163900, 180)
    SetChrPos(0x005B, 11700, -40, 163900, 180)
    SetChrPos(0x005C, 13540, -20, 163900, 180)
    SetChrPos(0x005D, 4000, -40, 166050, 180)
    SetChrPos(0x005E, 5930, 0, 166050, 180)
    SetChrPos(0x005F, 7900, 30, 166050, 180)
    SetChrPos(0x0060, 9800, 60, 166050, 180)
    SetChrPos(0x0061, 11700, 10, 166050, 180)
    SetChrPos(0x0062, 13540, -20, 166050, 180)
    SetChrPos(0x0067, -11510, -30, 157450, 180)
    SetChrPos(0x0068, -9600, -30, 157450, 180)
    SetChrPos(0x006D, -11510, -20, 159600, 180)
    SetChrPos(0x006E, -9600, -50, 159600, 180)
    SetChrPos(0x0073, -11510, -10, 161750, 180)
    SetChrPos(0x0074, -9600, -30, 161750, 180)
    SetChrPos(0x0079, -11510, -40, 163900, 180)
    SetChrPos(0x007A, -9600, -20, 163900, 180)
    SetChrPos(0x0063, -9600, -30, 168200, 180)
    SetChrPos(0x0064, -7630, -40, 168200, 180)
    SetChrPos(0x0065, -5660, 0, 168200, 180)
    SetChrPos(0x0066, -3630, 30, 168200, 180)
    SetChrPos(0x0069, -1730, 60, 168200, 180)
    SetChrPos(0x006A, 230, 10, 168200, 180)
    SetChrPos(0x006B, 2070, -20, 168200, 180)
    SetChrPos(0x006C, 4000, 30, 168200, 180)
    SetChrPos(0x006F, -9600, -30, 170350, 180)
    SetChrPos(0x0070, -7630, -40, 170350, 180)
    SetChrPos(0x0071, -5660, 0, 170350, 180)
    SetChrPos(0x0072, -3630, 30, 170350, 180)
    SetChrPos(0x0075, -1730, 60, 170350, 180)
    SetChrPos(0x0076, 230, 10, 170350, 180)
    SetChrPos(0x0077, 2070, -20, 170350, 180)
    SetChrPos(0x0078, 4000, 30, 170350, 180)
    ClearChrFlags(0x0045, 0x0080)
    ClearChrFlags(0x0046, 0x0080)
    ClearChrFlags(0x0047, 0x0080)
    ClearChrFlags(0x0048, 0x0080)
    ClearChrFlags(0x0049, 0x0080)
    ClearChrFlags(0x004A, 0x0080)
    ClearChrFlags(0x004B, 0x0080)
    ClearChrFlags(0x004C, 0x0080)
    ClearChrFlags(0x004D, 0x0080)
    ClearChrFlags(0x004E, 0x0080)
    ClearChrFlags(0x004F, 0x0080)
    ClearChrFlags(0x0050, 0x0080)
    ClearChrFlags(0x0051, 0x0080)
    ClearChrFlags(0x0052, 0x0080)
    ClearChrFlags(0x0053, 0x0080)
    ClearChrFlags(0x0054, 0x0080)
    ClearChrFlags(0x0055, 0x0080)
    ClearChrFlags(0x0056, 0x0080)
    ClearChrFlags(0x0057, 0x0080)
    ClearChrFlags(0x0058, 0x0080)
    ClearChrFlags(0x0059, 0x0080)
    ClearChrFlags(0x005A, 0x0080)
    ClearChrFlags(0x005B, 0x0080)
    ClearChrFlags(0x005C, 0x0080)
    ClearChrFlags(0x005D, 0x0080)
    ClearChrFlags(0x005E, 0x0080)
    ClearChrFlags(0x005F, 0x0080)
    ClearChrFlags(0x0060, 0x0080)
    ClearChrFlags(0x0061, 0x0080)
    ClearChrFlags(0x0062, 0x0080)
    ClearChrFlags(0x0063, 0x0080)
    ClearChrFlags(0x0064, 0x0080)
    ClearChrFlags(0x0065, 0x0080)
    ClearChrFlags(0x0066, 0x0080)
    ClearChrFlags(0x0067, 0x0080)
    ClearChrFlags(0x0068, 0x0080)
    ClearChrFlags(0x0069, 0x0080)
    ClearChrFlags(0x006A, 0x0080)
    ClearChrFlags(0x006B, 0x0080)
    ClearChrFlags(0x006C, 0x0080)
    ClearChrFlags(0x006D, 0x0080)
    ClearChrFlags(0x006E, 0x0080)
    ClearChrFlags(0x006F, 0x0080)
    ClearChrFlags(0x0070, 0x0080)
    ClearChrFlags(0x0071, 0x0080)
    ClearChrFlags(0x0072, 0x0080)
    ClearChrFlags(0x0073, 0x0080)
    ClearChrFlags(0x0074, 0x0080)
    ClearChrFlags(0x0075, 0x0080)
    ClearChrFlags(0x0076, 0x0080)
    ClearChrFlags(0x0077, 0x0080)
    ClearChrFlags(0x0078, 0x0080)
    ClearChrFlags(0x0079, 0x0080)
    ClearChrFlags(0x007A, 0x0080)
    ClearChrFlags(0x007B, 0x0080)
    ClearChrFlags(0x007C, 0x0080)
    ClearChrFlags(0x007D, 0x0080)
    ClearChrFlags(0x007E, 0x0080)

    @scena.Lambda('lambda_2A65')
    def lambda_2A65():
        OP_6D(-1410, 70, 152440, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A65)

    @scena.Lambda('lambda_2A7D')
    def lambda_2A7D():
        OP_6B(2600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A7D)

    OP_8C(0x000E, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000E,
        (
            '#0690380985V#885F#2P#3S全军撤退！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0690380986V#885F#2P#3S第３师团！\n',
            '全体向帕鲁姆市郊外移动！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    Sleep(800)

    SetMessageWindowPos(50, 90, -1, -1)
    SetChrName('帝国军士兵')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#4150380987V#5S是，长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_6D(-2140, 50, 142400, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrPos(0x0027, -7630, 0, 89450, 0)
    SetChrPos(0x0028, -5660, -50, 89450, 0)
    SetChrPos(0x0029, -3630, 0, 89450, 0)
    SetChrPos(0x002A, -1730, 90, 89450, 0)
    SetChrPos(0x002B, 230, -30, 89450, 0)
    SetChrPos(0x002C, 2070, -30, 89450, 0)
    SetChrPos(0x002D, -7630, 40, 91600, 0)
    SetChrPos(0x002E, -5660, 20, 91600, 0)
    SetChrPos(0x002F, -3630, -20, 91600, 0)
    SetChrPos(0x0030, -1730, 50, 91600, 0)
    SetChrPos(0x0031, 230, -20, 91600, 0)
    SetChrPos(0x0032, 2070, -50, 91600, 0)
    SetChrPos(0x0033, -7630, 30, 93750, 0)
    SetChrPos(0x0034, -5660, 10, 93750, 0)
    SetChrPos(0x0035, -3630, 20, 93750, 0)
    SetChrPos(0x0036, -1730, 70, 93750, 0)
    SetChrPos(0x0037, 230, -10, 93750, 0)
    SetChrPos(0x0038, 2070, -30, 93750, 0)
    SetChrPos(0x0039, -7630, -20, 95900, 0)
    SetChrPos(0x003A, -5660, -40, 95900, 0)
    SetChrPos(0x003B, -3630, -40, 95900, 0)
    SetChrPos(0x003C, -1730, 40, 95900, 0)
    SetChrPos(0x003D, 230, -40, 95900, 0)
    SetChrPos(0x003E, 2070, -20, 95900, 0)
    SetChrPos(0x003F, -7630, -40, 98050, 0)
    SetChrPos(0x0040, -5660, 0, 98050, 0)
    SetChrPos(0x0041, -3630, 30, 98050, 0)
    SetChrPos(0x0042, -1730, 60, 98050, 0)
    SetChrPos(0x0043, 230, 10, 98050, 0)
    SetChrPos(0x0044, 2070, -20, 98050, 0)
    SetChrPos(0x0045, 4000, 0, 89450, 0)
    SetChrPos(0x0046, 5930, -50, 89450, 0)
    SetChrPos(0x0047, 7900, 0, 89450, 0)
    SetChrPos(0x0048, 9800, 90, 89450, 0)
    SetChrPos(0x0049, 11700, -30, 89450, 0)
    SetChrPos(0x004A, 13540, -30, 89450, 0)
    SetChrPos(0x004B, 4000, 40, 91600, 0)
    SetChrPos(0x004C, 5930, 20, 91600, 0)
    SetChrPos(0x004D, 7900, -20, 91600, 0)
    SetChrPos(0x004E, 9800, 50, 91600, 0)
    SetChrPos(0x004F, 11700, -20, 91600, 0)
    SetChrPos(0x0050, 13540, -50, 91600, 0)
    SetChrPos(0x0051, 4000, 30, 93750, 0)
    SetChrPos(0x0052, 5930, 10, 93750, 0)
    SetChrPos(0x0053, 7900, 20, 93750, 0)
    SetChrPos(0x0054, 9800, 70, 93750, 0)
    SetChrPos(0x0055, 11700, -10, 93750, 0)
    SetChrPos(0x0056, 13540, -30, 93750, 0)
    SetChrPos(0x0057, 4000, -20, 95900, 0)
    SetChrPos(0x0058, 5930, -40, 95900, 0)
    SetChrPos(0x0059, 7900, -40, 95900, 0)
    SetChrPos(0x005A, 9800, 40, 95900, 0)
    SetChrPos(0x005B, 11700, -40, 95900, 0)
    SetChrPos(0x005C, 13540, -20, 95900, 0)
    SetChrPos(0x005D, 4000, -40, 98050, 0)
    SetChrPos(0x005E, 5930, 0, 98050, 0)
    SetChrPos(0x005F, 7900, 30, 98050, 0)
    SetChrPos(0x0060, 9800, 60, 98050, 0)
    SetChrPos(0x0061, 11700, 10, 98050, 0)
    SetChrPos(0x0062, 13540, -20, 98050, 0)
    SetChrPos(0x0063, -19030, 0, 89450, 0)
    SetChrPos(0x0064, -17150, -50, 89450, 0)
    SetChrPos(0x0065, -15270, 0, 89450, 0)
    SetChrPos(0x0066, -13390, 90, 89450, 0)
    SetChrPos(0x0067, -11510, -30, 89450, 0)
    SetChrPos(0x0068, -9600, -30, 89450, 0)
    SetChrPos(0x0069, -19030, 40, 91600, 0)
    SetChrPos(0x006A, -17150, 20, 91600, 0)
    SetChrPos(0x006B, -15270, -20, 91600, 0)
    SetChrPos(0x006C, -13390, 50, 91600, 0)
    SetChrPos(0x006D, -11510, -20, 91600, 0)
    SetChrPos(0x006E, -9600, -50, 91600, 0)
    SetChrPos(0x006F, -19030, 30, 93750, 0)
    SetChrPos(0x0070, -17150, 10, 93750, 0)
    SetChrPos(0x0071, -15270, 20, 93750, 0)
    SetChrPos(0x0072, -13390, 70, 93750, 0)
    SetChrPos(0x0073, -11510, -10, 93750, 0)
    SetChrPos(0x0074, -9600, -30, 93750, 0)
    SetChrPos(0x0075, -19030, -20, 95900, 0)
    SetChrPos(0x0076, -17150, -40, 95900, 0)
    SetChrPos(0x0077, -15270, -40, 95900, 0)
    SetChrPos(0x0078, -13390, 40, 95900, 0)
    SetChrPos(0x0079, -11510, -40, 95900, 0)
    SetChrPos(0x007A, -9600, -20, 95900, 0)
    SetChrPos(0x007B, -19030, -40, 98050, 0)
    SetChrPos(0x007C, -17150, 0, 98050, 0)
    SetChrPos(0x007D, -15270, 30, 98050, 0)
    SetChrPos(0x007E, -13390, 60, 98050, 0)
    SetChrChipByIndex(0x0015, 9)
    SetChrChipByIndex(0x0016, 9)
    SetChrSubChip(0x0015, 0)
    SetChrSubChip(0x0016, 0)
    SetChrFlags(0x0015, 0x0200)
    SetChrFlags(0x0016, 0x0200)
    SetChrPos(0x0015, -11510, 10, 98050, 0)
    SetChrPos(0x0016, -9600, -20, 98050, 0)
    OP_8C(0x0017, 180, 0)
    OP_8C(0x0018, 180, 0)
    OP_8C(0x0019, 180, 0)
    OP_8C(0x001A, 180, 0)
    OP_8C(0x001B, 180, 0)
    OP_8C(0x001C, 180, 0)
    OP_8C(0x001D, 180, 0)
    OP_8C(0x001E, 180, 0)
    OP_8C(0x001F, 180, 0)
    OP_8C(0x0020, 180, 0)
    OP_8C(0x0021, 180, 0)
    OP_8C(0x0022, 180, 0)
    OP_8C(0x0023, 180, 0)
    OP_8C(0x0024, 180, 0)
    LoadEffect(0x00, 'map\\\\mp109_00.eff')
    LoadEffect(0x01, 'map\\\\onsen00.eff')
    PlayEffect(0x00, 0xFF, 0x0017, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0017, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0018, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0018, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0019, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0019, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001A, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001A, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001B, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001B, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001C, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001C, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001D, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001D, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001E, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001E, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001F, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001F, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0020, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0020, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0021, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0021, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0022, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0022, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0023, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0023, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0024, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0024, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0017, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0017, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0018, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0018, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0019, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0019, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001A, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001A, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001B, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001B, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001C, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001C, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001D, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001D, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001E, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001E, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001F, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001F, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0020, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0020, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0021, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0021, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0022, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0022, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0023, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0023, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0024, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0024, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_6D(-2080, 50, 134590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrChipByIndex(0x0013, 13)
    SetChrChipByIndex(0x0012, 14)
    SetChrChipByIndex(0x0014, 15)
    OP_22(0x010F, 0x01, 0x64)
    OP_22(0x0110, 0x01, 0x5F)
    CreateThread(0x0017, 0x03, 0x01, 0x000E)
    WaitForThreadExit(0x0017, 0x0003)
    CreateThread(0x0027, 0x03, 0x01, 0x000F)
    CreateThread(0x0045, 0x03, 0x01, 0x0010)
    CreateThread(0x0063, 0x03, 0x01, 0x0011)
    WaitForThreadExit(0x0027, 0x0003)
    WaitForThreadExit(0x0045, 0x0003)
    WaitForThreadExit(0x0063, 0x0003)
    FadeIn(1000, 0)
    OP_6D(-1520, 20, 117830, 6000)
    Fade(1000)
    OP_6D(-920, 20, 89290, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    SetChrPos(0x000D, -1950, 40, 88980, 0)
    SetChrPos(0x0010, -600, 70, 88900, 0)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    OP_0D()
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    SetChrFlags(0x002D, 0x0080)
    SetChrFlags(0x002E, 0x0080)
    SetChrFlags(0x002F, 0x0080)
    SetChrFlags(0x0030, 0x0080)
    SetChrFlags(0x0031, 0x0080)
    SetChrFlags(0x0032, 0x0080)
    SetChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0034, 0x0080)
    SetChrFlags(0x0035, 0x0080)
    SetChrFlags(0x0036, 0x0080)
    SetChrFlags(0x0037, 0x0080)
    SetChrFlags(0x0038, 0x0080)
    SetChrFlags(0x0039, 0x0080)
    SetChrFlags(0x003A, 0x0080)
    SetChrFlags(0x003B, 0x0080)
    SetChrFlags(0x003C, 0x0080)
    SetChrFlags(0x003D, 0x0080)
    SetChrFlags(0x003E, 0x0080)
    SetChrFlags(0x003F, 0x0080)
    SetChrFlags(0x0040, 0x0080)
    SetChrFlags(0x0041, 0x0080)
    SetChrFlags(0x0042, 0x0080)
    SetChrFlags(0x0043, 0x0080)
    SetChrFlags(0x0044, 0x0080)
    SetChrFlags(0x0045, 0x0080)
    SetChrFlags(0x0046, 0x0080)
    SetChrFlags(0x0047, 0x0080)
    SetChrFlags(0x0048, 0x0080)
    SetChrFlags(0x0049, 0x0080)
    SetChrFlags(0x004A, 0x0080)
    SetChrFlags(0x004B, 0x0080)
    SetChrFlags(0x004C, 0x0080)
    SetChrFlags(0x004D, 0x0080)
    SetChrFlags(0x004E, 0x0080)
    SetChrFlags(0x004F, 0x0080)
    SetChrFlags(0x0050, 0x0080)
    SetChrFlags(0x0051, 0x0080)
    SetChrFlags(0x0052, 0x0080)
    SetChrFlags(0x0053, 0x0080)
    SetChrFlags(0x0054, 0x0080)
    SetChrFlags(0x0055, 0x0080)
    SetChrFlags(0x0056, 0x0080)
    SetChrFlags(0x0057, 0x0080)
    SetChrFlags(0x0058, 0x0080)
    SetChrFlags(0x0059, 0x0080)
    SetChrFlags(0x005A, 0x0080)
    SetChrFlags(0x005B, 0x0080)
    SetChrFlags(0x005C, 0x0080)
    SetChrFlags(0x005D, 0x0080)
    SetChrFlags(0x005E, 0x0080)
    SetChrFlags(0x005F, 0x0080)
    SetChrFlags(0x0060, 0x0080)
    SetChrFlags(0x0061, 0x0080)
    SetChrFlags(0x0062, 0x0080)
    SetChrFlags(0x0063, 0x0080)
    SetChrFlags(0x0064, 0x0080)
    SetChrFlags(0x0065, 0x0080)
    SetChrFlags(0x0066, 0x0080)
    SetChrFlags(0x0067, 0x0080)
    SetChrFlags(0x0068, 0x0080)
    SetChrFlags(0x0069, 0x0080)
    SetChrFlags(0x006A, 0x0080)
    SetChrFlags(0x006B, 0x0080)
    SetChrFlags(0x006C, 0x0080)
    SetChrFlags(0x006D, 0x0080)
    SetChrFlags(0x006E, 0x0080)
    SetChrFlags(0x006F, 0x0080)
    SetChrFlags(0x0070, 0x0080)
    SetChrFlags(0x0071, 0x0080)
    SetChrFlags(0x0072, 0x0080)
    SetChrFlags(0x0073, 0x0080)
    SetChrFlags(0x0074, 0x0080)
    SetChrFlags(0x0075, 0x0080)
    SetChrFlags(0x0076, 0x0080)
    SetChrFlags(0x0077, 0x0080)
    SetChrFlags(0x0078, 0x0080)
    SetChrFlags(0x0079, 0x0080)
    SetChrFlags(0x007A, 0x0080)
    SetChrFlags(0x007B, 0x0080)
    SetChrFlags(0x007C, 0x0080)
    SetChrFlags(0x007D, 0x0080)
    SetChrFlags(0x007E, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    OP_71(0x0003, 0x0000)
    OP_71(0x0004, 0x0000)
    OP_71(0x0005, 0x0000)
    OP_71(0x0006, 0x0000)
    OP_71(0x0007, 0x0000)
    OP_71(0x0008, 0x0000)
    OP_71(0x0009, 0x0000)
    OP_71(0x000A, 0x0000)
    OP_71(0x000B, 0x0000)
    OP_71(0x000C, 0x0000)
    OP_71(0x000D, 0x0000)
    OP_71(0x000E, 0x0000)
    OP_71(0x000F, 0x0000)
    OP_71(0x0010, 0x0000)
    CreateThread(0x000D, 0x03, 0x01, 0x0012)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x000D,
        (
            '#0040380988V#890F#6P哎呀哎呀……\n',
            '终于稍微争取了一点时间吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380989V#893F话说回来，我还\n',
            '真是没信用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0010, 270, 400)
    Sleep(300)

    ChrTalk(
        0x0010,
        (
            '#0110380990V#276F#2P……当然啦，蠢货。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110380991V#272F说实话，\n',
            '真没想到会闹得这么大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 90, 400)
    Sleep(300)

    ChrTalk(
        0x000D,
        (
            '#0040380992V#890F#6P既然要做，\n',
            '就要做得华丽啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380993V#891F而且你不是也\n',
            '早就做了准备吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380994V可以说是共同享受甜蜜结果的\n',
            '相亲相爱的共犯者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0110380995V#274F#2P别说得那么恶心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380996V#1P奥利维尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    Fade(500)
    OP_6D(-2560, 70, 87160, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(225000, 0)
    OP_6E(364, 0)

    @scena.Lambda('lambda_4376')
    def lambda_4376():
        OP_6D(-3120, -20, 84880, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4376)

    @scena.Lambda('lambda_438E')
    def lambda_438E():
        OP_6E(381, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_438E)

    CreateThread(0x0101, 0x01, 0x01, 0x0006)
    CreateThread(0x000C, 0x01, 0x01, 0x0007)
    CreateThread(0x0102, 0x01, 0x01, 0x0008)
    CreateThread(0x000A, 0x01, 0x01, 0x000B)
    CreateThread(0x0008, 0x01, 0x01, 0x0009)
    CreateThread(0x0009, 0x01, 0x01, 0x000A)
    CreateThread(0x000B, 0x01, 0x01, 0x000C)
    CreateThread(0x000F, 0x01, 0x01, 0x000D)
    OP_8C(0x000D, 180, 400)
    OP_8C(0x0010, 180, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000D,
        (
            '#0040380997V#891F#4P呀，艾丝蒂尔。\n',
            '你辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380998V#1009F#5P辛苦你个头啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380999V到底是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040381000V#890F#4P也没怎么回事啦，\n',
            '嗯，就和你看到的一样嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040381001V#891F因为帝国内正进行着\n',
            '可疑的阴谋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040381002V所以就稍微表演一下，\n',
            '挫挫他们的锐气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381003V#1019F#5P表演一下……你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040381004V#894F#4P要瞒过敌人\n',
            '首先得瞒过自己人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040381005V#890F先和你们认真交涉，\n',
            '然后埃尔赛尤出场……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040381006V这就是我和卡西乌斯先生\n',
            '想出来的剧本。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381007V#1007F#5P果、果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020381008V#1040F#5P就知道是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000F, 0x0001)
    ClearChrFlags(0x0011, 0x0020)
    OP_9F(0x0011, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0011, -17000, -130, 84330, 90)
    OP_9F(0x0011, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    NpcTalk(
        0x0011,
        '男性的声音',
        (
            '#0160381009V#3P……嗯，就是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0011, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_47A6')
    def lambda_47A6():
        OP_6D(-3420, -30, 84750, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_47A6)

    @scena.Lambda('lambda_47BE')
    def lambda_47BE():
        OP_6B(2590, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_47BE)

    @scena.Lambda('lambda_47CE')
    def lambda_47CE():
        OP_6C(224000, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_47CE)

    @scena.Lambda('lambda_47DE')
    def lambda_47DE():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_47DE')

    DispatchAsync2(0x000D, 0x0001, lambda_47DE)

    @scena.Lambda('lambda_47EF')
    def lambda_47EF():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_47EF')

    DispatchAsync2(0x0010, 0x0001, lambda_47EF)

    Sleep(50)

    @scena.Lambda('lambda_4805')
    def lambda_4805():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_4805')

    DispatchAsync2(0x000C, 0x0001, lambda_4805)

    @scena.Lambda('lambda_4816')
    def lambda_4816():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_4816')

    DispatchAsync2(0x0101, 0x0001, lambda_4816)

    Sleep(50)

    @scena.Lambda('lambda_482C')
    def lambda_482C():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_482C')

    DispatchAsync2(0x0102, 0x0001, lambda_482C)

    @scena.Lambda('lambda_483D')
    def lambda_483D():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_483D')

    DispatchAsync2(0x0009, 0x0001, lambda_483D)

    Sleep(50)

    @scena.Lambda('lambda_4853')
    def lambda_4853():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_4853')

    DispatchAsync2(0x0008, 0x0001, lambda_4853)

    @scena.Lambda('lambda_4864')
    def lambda_4864():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_4864')

    DispatchAsync2(0x000A, 0x0001, lambda_4864)

    Sleep(50)

    @scena.Lambda('lambda_487A')
    def lambda_487A():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_487A')

    DispatchAsync2(0x000B, 0x0001, lambda_487A)

    @scena.Lambda('lambda_488B')
    def lambda_488B():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_488B')

    DispatchAsync2(0x000F, 0x0001, lambda_488B)

    OP_8E(0x0011, -5710, -30, 85070, 3000, 0x00)
    OP_8C(0x0011, 90, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010381010V#1009F#6P老爸～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381011V#1123F#2P别摆出这么可怕的表情嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381012V#1120F我通过导力通信听到了，\n',
            '真是场相当不错的谈判啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381013V托你的福，埃尔赛尤的登场\n',
            '演出更有成效了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381014V#1004F#6P用导力通信听到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0x01)
    OP_8C(0x0008, 0, 400)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0030381015V#023F#5P难不成……\n',
            '用那个古代遗物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000D, 0x01)
    OP_8C(0x000D, 180, 400)
    Sleep(300)

    ChrTalk(
        0x000D,
        (
            '#0040381016V#891F#6P哟，雪拉。\n',
            '别说这个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040381017V被他听见的话\n',
            '稍微有点麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0014, -22110, -290, 84920, 90)
    SetChrPos(0x0012, -21810, -280, 83150, 90)
    SetChrPos(0x0013, -23280, -330, 83160, 90)

    NpcTalk(
        0x0014,
        '青年的声音',
        (
            '#0180381018V#3P……干嘛装模作样。\n',
            '事到如今，再想掩饰也太迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4AEE')
    def lambda_4AEE():
        OP_6D(-5560, 20, 84410, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4AEE)

    @scena.Lambda('lambda_4B06')
    def lambda_4B06():
        OP_67(0, 4530, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4B06)

    @scena.Lambda('lambda_4B1E')
    def lambda_4B1E():
        OP_6E(380, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4B1E)

    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)

    @scena.Lambda('lambda_4B3D')
    def lambda_4B3D():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4B3D')

    DispatchAsync2(0x000C, 0x0001, lambda_4B3D)

    @scena.Lambda('lambda_4B4E')
    def lambda_4B4E():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4B4E')

    DispatchAsync2(0x0101, 0x0001, lambda_4B4E)

    @scena.Lambda('lambda_4B5F')
    def lambda_4B5F():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4B5F')

    DispatchAsync2(0x0102, 0x0001, lambda_4B5F)

    Sleep(100)

    @scena.Lambda('lambda_4B75')
    def lambda_4B75():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4B75')

    DispatchAsync2(0x0009, 0x0001, lambda_4B75)

    @scena.Lambda('lambda_4B86')
    def lambda_4B86():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4B86')

    DispatchAsync2(0x0008, 0x0001, lambda_4B86)

    Sleep(100)

    @scena.Lambda('lambda_4B9C')
    def lambda_4B9C():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4B9C')

    DispatchAsync2(0x000A, 0x0001, lambda_4B9C)

    @scena.Lambda('lambda_4BAD')
    def lambda_4BAD():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4BAD')

    DispatchAsync2(0x000B, 0x0001, lambda_4BAD)

    @scena.Lambda('lambda_4BBE')
    def lambda_4BBE():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4BBE')

    DispatchAsync2(0x000F, 0x0001, lambda_4BBE)

    Sleep(100)

    @scena.Lambda('lambda_4BD4')
    def lambda_4BD4():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4BD4')

    DispatchAsync2(0x000D, 0x0001, lambda_4BD4)

    @scena.Lambda('lambda_4BE5')
    def lambda_4BE5():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_4BE5')

    DispatchAsync2(0x0010, 0x0001, lambda_4BE5)

    @scena.Lambda('lambda_4BF6')
    def lambda_4BF6():
        OP_8E(0x00FE, -6310, -10, 86000, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_4BF6)

    Sleep(400)

    @scena.Lambda('lambda_4C16')
    def lambda_4C16():
        OP_8E(0x00FE, -6280, -10, 83630, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_4C16)

    Sleep(400)

    @scena.Lambda('lambda_4C36')
    def lambda_4C36():
        OP_8E(0x00FE, -7800, -10, 83950, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_4C36)

    WaitForThreadExit(0x0014, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0102, 0x01)

    @scena.Lambda('lambda_4C63')
    def lambda_4C63():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4C63)

    Sleep(50)

    @scena.Lambda('lambda_4C76')
    def lambda_4C76():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4C76)

    ChrTalk(
        0x0101,
        (
            '#0010381019V#1004F#6P凯、凯文先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070381020V#560F#6P爷，爷爷！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060381021V#1168F#6P还有尤莉亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0013, 0x0001)

    ChrTalk(
        0x0013,
        (
            '#0100381022V#176F殿下……\n',
            '我听说王都被袭击了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100381023V#175F不过……您没事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060381024V#1169F#6P对不起……\n',
            '让你担心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0540381025V#101F#5P呀～埃尔赛尤的改造\n',
            '如果能早些完成，王都的危机也\n',
            '就不至于这么晚才解决了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540381026V比预想中\n',
            '花费了更多时间啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540381027V#100F不过，大家都没事就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050381028V#055F#6P话，话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050381029V为何埃尔赛尤\n',
            '能飞上天空！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070381030V#560F#6P难不成……\n',
            '『零力场发生器』的大型版开发出来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0540381031V#101F#5P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540381032V#100F给你们的是\n',
            '为了开发大型版\n',
            '而试制的原型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540381033V至今为止我都在埃尔赛尤上\n',
            '闭关研究，总算是完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020381034V#1040F#6P原来是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381035V#1019F#6P也就是说，一切\n',
            '都是老爸设的局了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381036V#1123F#2P别说得这么伤人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381037V#1120F我只不过为了方便大家行动\n',
            '而做了各种准备而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381038V你们也一直都是\n',
            '按照自己的意思行事的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381039V#1015F#6P话，话是没错啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010381040V#1004F那，凯文先生\n',
            '又为什么会在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180381041V#1062F#2P啊啊，其实大圣堂\n',
            '收到了骑士团本部的联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180381042V『辉之环』到底是怎样的东西，\n',
            '怎样才能控制灾难，\n',
            '现在大致都明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180381043V#1061F将情况告知给卡西乌斯先生之后\n',
            '我就一起跟过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381044V#1020F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020381045V#1042F#6P『辉之环』的正体……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180381046V#1065F#2P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180381047V#1063F所谓『辉之环』\n',
            '并不是那个浮游都市本身。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180381048V而是引导都市全体的导力走向，\n',
            '并且加以控制的古代遗物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180381049V而其终端\n',
            '就是那个『福音』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060381050V#1163F#6P管理都市的古代遗物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070381051V#065F#6P但、但是为什么\n',
            '那东西会引起导力停止现象？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180381052V#1067F#2P现在只是推测……\n',
            '环似乎具备排除\n',
            '外界异物的功能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180381053V#1063F在如今的情况下，所谓的异物\n',
            '就是现代所创造的新导力器──\n',
            '也就是Orbment。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080381054V#074F#6P将影响范围内的异物\n',
            '全部无力化……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080381055V#072F可以说这是一种防卫架构吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0540381056V#104F#5P这个可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540381057V#102F而如果这是真的，\n',
            '就可以看见一线光明了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540381058V由于过于巨大，要对都市本身\n',
            '进行全面处理非常困难……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540381059V但如果能够找到在存放于都市\n',
            '某处的环的实体，\n',
            '应该就能进行对策了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020381060V#1040F#6P原来如此……\n',
            '是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381061V#1006F#6P的、的确可能有希望……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040381062V#891F#6P嗯，这下最终目的\n',
            '不就能确定了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040381063V#890F那么就马上乘上『埃尔赛尤』\n',
            '前往那个浮游都市吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381064V#1125F#2P要做这个决定，\n',
            '得看拥有『埃尔赛尤』的\n',
            '利贝尔王室了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381065V#1122F公主殿下……请下决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060381066V#1167F#6P……我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060381067V#1162F现在开始，『埃尔赛尤』\n',
            '就向瓦雷利亚湖上出现的\n',
            '古代浮游都市前进。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060381068V尤莉亚上尉，准备起飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0100381069V#171F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0013, 270, 400)

    @scena.Lambda('lambda_577C')
    def lambda_577C():
        OP_8E(0x00FE, -23280, -330, 83160, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_577C)

    @scena.Lambda('lambda_5797')
    def lambda_5797():
        OP_6D(-3610, -30, 83240, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5797)

    @scena.Lambda('lambda_57AF')
    def lambda_57AF():
        OP_67(0, 4980, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_57AF)

    @scena.Lambda('lambda_57C7')
    def lambda_57C7():
        OP_6B(2450, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_57C7)

    @scena.Lambda('lambda_57D7')
    def lambda_57D7():
        OP_6C(224000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_57D7)

    @scena.Lambda('lambda_57E7')
    def lambda_57E7():
        OP_6E(354, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_57E7)

    TerminateThread(0x000C, 0x01)
    OP_8C(0x000C, 215, 400)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0060381070V#1167F#6P还有各位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5839')
    def lambda_5839():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5839)

    @scena.Lambda('lambda_5847')
    def lambda_5847():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5847)

    Sleep(50)

    @scena.Lambda('lambda_585A')
    def lambda_585A():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_585A)

    @scena.Lambda('lambda_5868')
    def lambda_5868():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5868)

    Sleep(50)

    @scena.Lambda('lambda_587B')
    def lambda_587B():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_587B)

    @scena.Lambda('lambda_5889')
    def lambda_5889():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5889)

    @scena.Lambda('lambda_5897')
    def lambda_5897():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5897)

    Sleep(50)

    @scena.Lambda('lambda_58AA')
    def lambda_58AA():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_58AA)

    @scena.Lambda('lambda_58B8')
    def lambda_58B8():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_58B8)

    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0060381071V#1162F#6P请向困境中的利贝尔\n',
            '伸出各位的援助之手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060381072V这恐怕是关于这次事件的\n',
            '最后委托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030381073V#027F#5P呵呵……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050381074V#051F#5P嗯，答案简直\n',
            '就是不言自明嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080381075V#071F#5P现在就请一个\n',
            '代表来回答吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010381076V#1015F#4P嗯……代表？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0050381077V#053F#5P我说……艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050381078V#555F当然是说你吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5A56')
    def lambda_5A56():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5A56)

    Sleep(50)

    @scena.Lambda('lambda_5A69')
    def lambda_5A69():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_5A69)

    Sleep(50)

    OP_8C(0x000A, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010381079V#1004F#4P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030381080V#021F#5P呵呵……\n',
            '你那是什么表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030381081V#524F确实，虽然大家\n',
            '各有各的目的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030381082V但是，不管怎么说\n',
            '我们大家都是和你\n',
            '共同分享旅途的同伴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080381083V#070F#5P这个意义上来说，艾丝蒂尔，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080381084V你毫无疑问\n',
            '就是我们的领导人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381085V#1013F#4P啊，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381086V#1123F#2P哎呀哎呀……\n',
            '是觉得担子太重了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020381087V#1035F#5P……不是那样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020381088V#1040F无论在任何时候，艾丝蒂尔都是那么乐观，\n',
            '从不会放弃希望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020381089V那耀眼的光辉自始至终都在\n',
            '指引着我──还有大家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020381090V#1049F所以……\n',
            '一定要是艾丝蒂尔才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010381091V#1013F#4P等、等一下啦约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070381092V#061F#6P嘿嘿……\n',
            '姐姐，你的脸通红了哟？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381093V#1013F#4P～～～呜～～～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010381094V#1022F啊～真是的，知道了啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010381095V#1006F#2P科洛丝的委托……\n',
            '就让我们接受吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010381096V我们一定会找到\n',
            '那个浮游都市中的『辉之环』，\n',
            '并解决如今的事态！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '科洛丝',
        (
            '#0060381097V#1168F呵呵……\n',
            '拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381098V#1120F#2P哎呀哎呀……\n',
            '终于整理好思路了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381099V这样我也终于\n',
            '能返回司令部了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5EFA')
    def lambda_5EFA():
        OP_6D(-4960, 10, 83700, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5EFA)

    @scena.Lambda('lambda_5F12')
    def lambda_5F12():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F12')

    DispatchAsync2(0x0101, 0x0001, lambda_5F12)

    @scena.Lambda('lambda_5F23')
    def lambda_5F23():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F23')

    DispatchAsync2(0x0102, 0x0001, lambda_5F23)

    Sleep(50)

    @scena.Lambda('lambda_5F39')
    def lambda_5F39():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F39')

    DispatchAsync2(0x000C, 0x0001, lambda_5F39)

    @scena.Lambda('lambda_5F4A')
    def lambda_5F4A():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F4A')

    DispatchAsync2(0x0009, 0x0001, lambda_5F4A)

    @scena.Lambda('lambda_5F5B')
    def lambda_5F5B():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F5B')

    DispatchAsync2(0x0008, 0x0001, lambda_5F5B)

    Sleep(50)

    @scena.Lambda('lambda_5F71')
    def lambda_5F71():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F71')

    DispatchAsync2(0x000B, 0x0001, lambda_5F71)

    @scena.Lambda('lambda_5F82')
    def lambda_5F82():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F82')

    DispatchAsync2(0x000A, 0x0001, lambda_5F82)

    Sleep(50)

    @scena.Lambda('lambda_5F98')
    def lambda_5F98():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5F98')

    DispatchAsync2(0x000B, 0x0001, lambda_5F98)

    @scena.Lambda('lambda_5FA9')
    def lambda_5FA9():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5FA9')

    DispatchAsync2(0x000F, 0x0001, lambda_5FA9)

    Sleep(50)

    @scena.Lambda('lambda_5FBF')
    def lambda_5FBF():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5FBF')

    DispatchAsync2(0x000D, 0x0001, lambda_5FBF)

    @scena.Lambda('lambda_5FD0')
    def lambda_5FD0():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_5FD0')

    DispatchAsync2(0x0010, 0x0001, lambda_5FD0)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010381100V#1025F#6P老爸……你果然\n',
            '不和我们一起来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381101V#1125F#2P啊啊……抱歉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381102V#1122F虽说暂时撤退了，\n',
            '但帝国军的威胁仍不能忽视。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381103V不仅仅是哈肯大门，\n',
            '也可能会有来自海上的攻击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381104V当然，在王都发生的\n',
            '『结社』的袭击可能也会再次出现吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381105V在这种状况下，我是不能\n',
            '离开王国军的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381106V#1012F#6P嗯……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010381107V#1017F我也会加油的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010381108V和约修亚……\n',
            '还有大家一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010381109V因此老爸也要……\n',
            '在身体能承受的范围内好好努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381110V#1120F#2P啊啊……放心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381111V#1125F约修亚……\n',
            '这个交给你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020381112V#1044F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6267')
    def lambda_6267():
        OP_8F(0x00FE, -4840, -10, 84830, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_6267)

    Sleep(300)

    TerminateThread(0x0102, 0x01)
    OP_8F(0x0102, -4040, -10, 84540, 1000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    Fade(250)
    SetChrFlags(0x0011, 0x0002)
    SetChrChipByIndex(0x0011, 16)
    SetChrSubChip(0x0011, 0)
    OP_0D()
    Sleep(300)

    SetChrSubChip(0x0011, 1)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯交给约修亚一封信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(100)

    Fade(250)
    ClearChrFlags(0x0011, 0x0002)
    SetChrSubChip(0x0011, 0)
    SetChrChipByIndex(0x0011, 11)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0102,
        (
            '#0020381113V#1044F#6P这是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381114V#1125F#2P嗯，为父的一点关心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381115V#1120F这可是男人之间的对话，\n',
            '就不要让艾丝蒂尔被刺激到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381116V#1019F#6P什、什么意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020381117V#1040F#6P……明白了。\n',
            '我稍后再看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160381118V#1120F#2P啊啊，这样就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381119V#1007F#6P真受不了……\n',
            '男人总是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_648B')
    def lambda_648B():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_648B)

    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0160381120V#1123F#2P好了，别闹别扭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381121V#1120F等一切都解决之后，\n',
            '我也打算休假了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381122V到时候就可以\n',
            '悠闲自在地在家休息一阵了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381123V#1121F到时候，艾丝蒂尔，\n',
            '再给我做那个煎蛋卷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010381124V#1004F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010381125V#1017F……嗯，包在我身上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    SetChrFlags(0x002D, 0x0080)
    SetChrFlags(0x002E, 0x0080)
    SetChrFlags(0x002F, 0x0080)
    SetChrFlags(0x0030, 0x0080)
    SetChrFlags(0x0031, 0x0080)
    SetChrFlags(0x0032, 0x0080)
    SetChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0034, 0x0080)
    SetChrFlags(0x0035, 0x0080)
    SetChrFlags(0x0036, 0x0080)
    SetChrFlags(0x0037, 0x0080)
    SetChrFlags(0x0038, 0x0080)
    SetChrFlags(0x0039, 0x0080)
    SetChrFlags(0x003A, 0x0080)
    SetChrFlags(0x003B, 0x0080)
    SetChrFlags(0x003C, 0x0080)
    SetChrFlags(0x003D, 0x0080)
    SetChrFlags(0x003E, 0x0080)
    SetChrFlags(0x003F, 0x0080)
    SetChrFlags(0x0040, 0x0080)
    SetChrFlags(0x0041, 0x0080)
    SetChrFlags(0x0042, 0x0080)
    SetChrFlags(0x0043, 0x0080)
    SetChrFlags(0x0044, 0x0080)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_6D(-31630, -180, 59850, 0)
    OP_67(0, 10310, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(156000, 0)
    OP_6E(628, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x0077, 0x00, 0x64)
    OP_22(0x0125, 0x00, 0x64)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x00000096)

    @scena.Lambda('lambda_6754')
    def lambda_6754():
        OP_6D(-26030, 2970, 49440, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6754)

    @scena.Lambda('lambda_676C')
    def lambda_676C():
        OP_67(0, 9640, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_676C)

    @scena.Lambda('lambda_6784')
    def lambda_6784():
        OP_6E(600, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6784)

    @scena.Lambda('lambda_6794')
    def lambda_6794():
        OP_6C(138000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6794)

    @scena.Lambda('lambda_67A4')
    def lambda_67A4():
        OP_6B(6000, 10000)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_67A4)

    CreateThread(0x0025, 0x00, 0x01, 0x0003)
    PlayEffect(0x00, 0x00, 0x00FF, -39070, -150, 58410, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00CC, 0x00, 0x64)
    OP_73(0x0002)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 150)
    OP_70(0x0002, 0x0000014A)
    Sleep(1500)

    OP_22(0x00DD, 0x00, 0x64)
    OP_74(0x0011, 0x00000000, 0x0001)
    Sleep(180)

    OP_74(0x0011, 0x00000000, 0x0002)
    Sleep(170)

    OP_22(0x00DD, 0x00, 0x64)
    OP_74(0x0011, 0x00000000, 0x0003)
    Sleep(180)

    OP_74(0x0011, 0x00000000, 0x0004)
    Sleep(170)

    OP_22(0x00DD, 0x00, 0x64)
    OP_74(0x0011, 0x00000000, 0x0005)
    Sleep(180)

    OP_74(0x0011, 0x00000000, 0x0006)
    Sleep(170)

    OP_74(0x0011, 0x00000000, 0x0007)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x3C)
    OP_6F(0x0002, 330)
    OP_70(0x0002, 0x000001AE)

    @scena.Lambda('lambda_6896')
    def lambda_6896():
        OP_8C(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_6896)

    @scena.Lambda('lambda_68A4')
    def lambda_68A4():
        OP_8C(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_68A4)

    Sleep(300)

    @scena.Lambda('lambda_68B7')
    def lambda_68B7():
        OP_8C(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_68B7)

    @scena.Lambda('lambda_68C5')
    def lambda_68C5():
        OP_8C(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_68C5)

    Sleep(200)

    @scena.Lambda('lambda_68D8')
    def lambda_68D8():
        OP_8C(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_68D8)

    @scena.Lambda('lambda_68E6')
    def lambda_68E6():
        OP_8C(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_68E6)

    Sleep(100)

    @scena.Lambda('lambda_68F9')
    def lambda_68F9():
        OP_8C(0x00FE, 180, 40)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_68F9)

    @scena.Lambda('lambda_6907')
    def lambda_6907():
        OP_8C(0x00FE, 180, 40)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_6907)

    Sleep(1500)

    @scena.Lambda('lambda_691A')
    def lambda_691A():
        OP_8C(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_691A)

    @scena.Lambda('lambda_6928')
    def lambda_6928():
        OP_8C(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_6928)

    Sleep(500)

    @scena.Lambda('lambda_693B')
    def lambda_693B():
        OP_8C(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_693B)

    @scena.Lambda('lambda_6949')
    def lambda_6949():
        OP_8C(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_6949)

    WaitForThreadExit(0x0025, 0x0000)
    WaitForThreadExit(0x0025, 0x0002)
    WaitForThreadExit(0x0026, 0x0002)
    OP_82(0x00, 0x02)
    OP_23(0x00CC)
    Sleep(1500)

    @scena.Lambda('lambda_6971')
    def lambda_6971():
        OP_6D(-35800, 0, 22420, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6971)

    @scena.Lambda('lambda_6989')
    def lambda_6989():
        OP_67(0, 6500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6989)

    @scena.Lambda('lambda_69A1')
    def lambda_69A1():
        OP_6E(469, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_69A1)

    @scena.Lambda('lambda_69B1')
    def lambda_69B1():
        OP_6C(174000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_69B1)

    @scena.Lambda('lambda_69C1')
    def lambda_69C1():
        OP_6B(8000, 2000)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_69C1)

    @scena.Lambda('lambda_69D1')
    def lambda_69D1():
        OP_8F(0x00FE, -46560, 50000, -358410, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_69D1)

    @scena.Lambda('lambda_69EC')
    def lambda_69EC():
        OP_8F(0x00FE, -46560, 5000, -358410, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_69EC)

    Sleep(50)

    @scena.Lambda('lambda_6A0C')
    def lambda_6A0C():
        OP_8F(0x00FE, -46560, 50000, -358410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6A0C)

    @scena.Lambda('lambda_6A27')
    def lambda_6A27():
        OP_8F(0x00FE, -46560, 5000, -358410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6A27)

    Sleep(50)

    @scena.Lambda('lambda_6A47')
    def lambda_6A47():
        OP_8F(0x00FE, -46560, 50000, -358410, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6A47)

    @scena.Lambda('lambda_6A62')
    def lambda_6A62():
        OP_8F(0x00FE, -46560, 5000, -358410, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6A62)

    Sleep(50)

    @scena.Lambda('lambda_6A82')
    def lambda_6A82():
        OP_8F(0x00FE, -46560, 50000, -358410, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6A82)

    @scena.Lambda('lambda_6A9D')
    def lambda_6A9D():
        OP_8F(0x00FE, -46560, 5000, -358410, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6A9D)

    Sleep(50)

    @scena.Lambda('lambda_6ABD')
    def lambda_6ABD():
        OP_8F(0x00FE, -46560, 50000, -358410, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6ABD)

    @scena.Lambda('lambda_6AD8')
    def lambda_6AD8():
        OP_8F(0x00FE, -46560, 5000, -358410, 14500, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6AD8)

    Sleep(50)

    @scena.Lambda('lambda_6AF8')
    def lambda_6AF8():
        OP_8F(0x00FE, -46560, 60000, -358410, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6AF8)

    @scena.Lambda('lambda_6B13')
    def lambda_6B13():
        OP_8F(0x00FE, -46560, 5000, -358410, 20500, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6B13)

    Sleep(50)

    OP_24(0x0125, 0x5A)
    OP_24(0x0077, 0x5A)

    @scena.Lambda('lambda_6B3B')
    def lambda_6B3B():
        OP_8F(0x00FE, -46560, 70000, -358410, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6B3B)

    @scena.Lambda('lambda_6B56')
    def lambda_6B56():
        OP_8F(0x00FE, -46560, 5000, -358410, 28500, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6B56)

    Sleep(50)

    @scena.Lambda('lambda_6B76')
    def lambda_6B76():
        OP_8F(0x00FE, -46560, 80000, -358410, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6B76)

    @scena.Lambda('lambda_6B91')
    def lambda_6B91():
        OP_8F(0x00FE, -46560, 5000, -358410, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6B91)

    Sleep(50)

    @scena.Lambda('lambda_6BB1')
    def lambda_6BB1():
        OP_8F(0x00FE, -46560, 90000, -358410, 45000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6BB1)

    @scena.Lambda('lambda_6BCC')
    def lambda_6BCC():
        OP_8F(0x00FE, -46560, 5000, -358410, 45000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6BCC)

    Sleep(50)

    @scena.Lambda('lambda_6BEC')
    def lambda_6BEC():
        OP_8F(0x00FE, -46560, 100000, -358410, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6BEC)

    @scena.Lambda('lambda_6C07')
    def lambda_6C07():
        OP_8F(0x00FE, -46560, 5000, -358410, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6C07)

    Sleep(150)

    OP_24(0x0125, 0x50)
    OP_24(0x0077, 0x50)
    Sleep(300)

    OP_24(0x0125, 0x46)
    OP_24(0x0077, 0x46)
    Sleep(300)

    OP_24(0x0125, 0x3C)
    OP_24(0x0077, 0x3C)
    Sleep(300)

    OP_24(0x0125, 0x32)
    OP_24(0x0077, 0x32)
    FadeOut(1000, 0, -1)
    Sleep(300)

    OP_24(0x0125, 0x28)
    OP_24(0x0077, 0x28)
    Sleep(300)

    OP_24(0x0125, 0x1E)
    OP_24(0x0077, 0x1E)
    Sleep(300)

    OP_24(0x0125, 0x14)
    OP_24(0x0077, 0x14)
    Sleep(300)

    OP_23(0x0125)
    OP_23(0x0077)
    OP_0D()
    OP_DC()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T1400._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x6C9B
@scena.Code('func_03_6C9B')
def func_03_6C9B():
    Sleep(1500)

    @scena.Lambda('lambda_6CA6')
    def lambda_6CA6():
        OP_8F(0x00FE, -40000, 5000, 65080, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6CA6)

    @scena.Lambda('lambda_6CC1')
    def lambda_6CC1():
        OP_8F(0x00FE, -40000, 20000, 65080, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6CC1)

    Sleep(700)

    @scena.Lambda('lambda_6CE1')
    def lambda_6CE1():
        OP_8F(0x00FE, -40000, 5000, 65080, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_6CE1)

    @scena.Lambda('lambda_6CFC')
    def lambda_6CFC():
        OP_8F(0x00FE, -40000, 20000, 65080, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6CFC)

    Sleep(500)

    @scena.Lambda('lambda_6D1C')
    def lambda_6D1C():
        OP_8F(0x00FE, -40000, 20000, 65080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6D1C)

    Sleep(300)

    @scena.Lambda('lambda_6D3C')
    def lambda_6D3C():
        OP_8F(0x00FE, -40000, 20000, 65080, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6D3C)

    Sleep(1000)

    @scena.Lambda('lambda_6D5C')
    def lambda_6D5C():
        OP_8F(0x00FE, -40000, 20000, 65080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6D5C)

    WaitForThreadExit(0x0025, 0x0001)
    WaitForThreadExit(0x0026, 0x0001)

    Return()

# id: 0x0004 offset: 0x6D7C
@scena.Code('func_04_6D7C')
def func_04_6D7C():
    OP_72(0x0002, 0x0020)
    OP_73(0x0002)
    OP_6F(0x0002, 430)
    OP_70(0x0002, 0x00000258)
    Sleep(1000)

    OP_75(0x0B, 0x00000000, 0x02)
    OP_22(0x00DD, 0x00, 0x64)
    Sleep(240)

    OP_22(0x00DD, 0x00, 0x64)
    Sleep(240)

    OP_22(0x00DD, 0x00, 0x64)
    Sleep(240)

    OP_73(0x0002)
    OP_6F(0x0002, 600)
    OP_70(0x0002, 0x00000320)
    OP_73(0x0002)

    Return()

# id: 0x0005 offset: 0x6DD1
@scena.Code('func_05_6DD1')
def func_05_6DD1():
    Sleep(2600)

    OP_75(0x0B, 0x00000000, 0x02)
    OP_74(0x0011, 0x00000000, 0x0006)
    Sleep(150)

    OP_74(0x0011, 0x00000000, 0x0005)
    Sleep(150)

    OP_74(0x0011, 0x00000000, 0x0004)
    Sleep(150)

    OP_74(0x0011, 0x00000000, 0x0003)
    Sleep(150)

    OP_74(0x0011, 0x00000000, 0x0002)
    Sleep(150)

    OP_74(0x0011, 0x00000000, 0x0001)
    Sleep(150)

    OP_74(0x0011, 0x00000000, 0x0000)

    Return()

# id: 0x0006 offset: 0x6E3B
@scena.Code('func_06_6E3B')
def func_06_6E3B():
    SetChrPos(0x00FE, -2790, 20, 65540, 0)
    OP_8E(0x00FE, -2790, 20, 85530, 5000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0007 offset: 0x6E68
@scena.Code('func_07_6E68')
def func_07_6E68():
    SetChrChipByIndex(0x00FE, 17)
    SetChrPos(0x00FE, -1370, 0, 65129, 0)
    OP_8E(0x00FE, -1370, 40, 85610, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 4)
    SetChrSubChip(0x00FE, 0)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0008 offset: 0x6EA4
@scena.Code('func_08_6EA4')
def func_08_6EA4():
    SetChrPos(0x00FE, -2950, 20, 63670, 0)
    OP_8E(0x00FE, -2950, -60, 84170, 5000, 0x00)
    SetChrSubChip(0x00FE, 0)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0009 offset: 0x6ED6
@scena.Code('func_09_6ED6')
def func_09_6ED6():
    SetChrChipByIndex(0x00FE, 18)
    SetChrPos(0x00FE, -1710, 30, 62720, 0)
    OP_8E(0x00FE, -1710, 30, 84020, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 0)
    SetChrSubChip(0x00FE, 0)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000A offset: 0x6F12
@scena.Code('func_0A_6F12')
def func_0A_6F12():
    SetChrChipByIndex(0x00FE, 19)
    SetChrPos(0x00FE, -520, 30, 61080, 0)
    OP_8E(0x00FE, -520, -10, 83550, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 1)
    SetChrSubChip(0x00FE, 0)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000B offset: 0x6F4E
@scena.Code('func_0B_6F4E')
def func_0B_6F4E():
    SetChrChipByIndex(0x00FE, 20)
    SetChrPos(0x00FE, -860, 10, 62910, 0)
    OP_8E(0x00FE, -860, 0, 84770, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 2)
    SetChrSubChip(0x00FE, 0)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000C offset: 0x6F8A
@scena.Code('func_0C_6F8A')
def func_0C_6F8A():
    SetChrChipByIndex(0x00FE, 21)
    SetChrPos(0x00FE, -2670, 30, 60510, 0)
    OP_8E(0x00FE, -2670, 30, 82660, 5000, 0x00)
    SetChrChipByIndex(0x00FE, 3)
    SetChrSubChip(0x00FE, 0)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x6FC6
@scena.Code('func_0D_6FC6')
def func_0D_6FC6():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -1890, 40, 61000, 0)
    OP_8E(0x00FE, -1890, 40, 81230, 3000, 0x00)
    SetChrSubChip(0x00FE, 0)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x6FFD
@scena.Code('func_0E_6FFD')
def func_0E_6FFD():
    @scena.Lambda('lambda_7003')
    def lambda_7003():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_7003)

    Sleep(160)

    @scena.Lambda('lambda_7023')
    def lambda_7023():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_7023)

    @scena.Lambda('lambda_703E')
    def lambda_703E():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_703E)

    Sleep(200)

    @scena.Lambda('lambda_705E')
    def lambda_705E():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_705E)

    @scena.Lambda('lambda_7079')
    def lambda_7079():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_7079)

    Sleep(180)

    @scena.Lambda('lambda_7099')
    def lambda_7099():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_7099)

    @scena.Lambda('lambda_70B4')
    def lambda_70B4():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_70B4)

    Sleep(230)

    @scena.Lambda('lambda_70D4')
    def lambda_70D4():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_70D4)

    @scena.Lambda('lambda_70EF')
    def lambda_70EF():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_70EF)

    Sleep(150)

    @scena.Lambda('lambda_710F')
    def lambda_710F():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_710F)

    @scena.Lambda('lambda_712A')
    def lambda_712A():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_712A)

    Sleep(190)

    @scena.Lambda('lambda_714A')
    def lambda_714A():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_714A)

    @scena.Lambda('lambda_7165')
    def lambda_7165():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_7165)

    Sleep(220)

    @scena.Lambda('lambda_7185')
    def lambda_7185():
        OP_91(0x00FE, 0, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_7185)

    Return()

# id: 0x000F offset: 0x719B
@scena.Code('func_0F_719B')
def func_0F_719B():
    @scena.Lambda('lambda_71A1')
    def lambda_71A1():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003F, 0x0001, lambda_71A1)

    @scena.Lambda('lambda_71BC')
    def lambda_71BC():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0041, 0x0001, lambda_71BC)

    Sleep(100)

    @scena.Lambda('lambda_71DC')
    def lambda_71DC():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0040, 0x0001, lambda_71DC)

    Sleep(80)

    @scena.Lambda('lambda_71FC')
    def lambda_71FC():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0042, 0x0001, lambda_71FC)

    @scena.Lambda('lambda_7217')
    def lambda_7217():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_7217)

    Sleep(70)

    @scena.Lambda('lambda_7237')
    def lambda_7237():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0043, 0x0001, lambda_7237)

    Sleep(30)

    @scena.Lambda('lambda_7257')
    def lambda_7257():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_7257)

    Sleep(90)

    @scena.Lambda('lambda_7277')
    def lambda_7277():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7277)

    @scena.Lambda('lambda_7292')
    def lambda_7292():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003E, 0x0001, lambda_7292)

    @scena.Lambda('lambda_72AD')
    def lambda_72AD():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_72AD)

    Sleep(40)

    @scena.Lambda('lambda_72CD')
    def lambda_72CD():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_72CD)

    @scena.Lambda('lambda_72E8')
    def lambda_72E8():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_72E8)

    Sleep(30)

    @scena.Lambda('lambda_7308')
    def lambda_7308():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7308)

    @scena.Lambda('lambda_7323')
    def lambda_7323():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0036, 0x0001, lambda_7323)

    Sleep(70)

    @scena.Lambda('lambda_7343')
    def lambda_7343():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0035, 0x0001, lambda_7343)

    @scena.Lambda('lambda_735E')
    def lambda_735E():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_735E)

    Sleep(40)

    @scena.Lambda('lambda_737E')
    def lambda_737E():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_737E)

    @scena.Lambda('lambda_7399')
    def lambda_7399():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_7399)

    @scena.Lambda('lambda_73B4')
    def lambda_73B4():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_73B4)

    Sleep(50)

    @scena.Lambda('lambda_73D4')
    def lambda_73D4():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_73D4)

    @scena.Lambda('lambda_73EF')
    def lambda_73EF():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_73EF)

    Sleep(30)

    @scena.Lambda('lambda_740F')
    def lambda_740F():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_740F)

    Sleep(100)

    @scena.Lambda('lambda_742F')
    def lambda_742F():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002E, 0x0001, lambda_742F)

    @scena.Lambda('lambda_744A')
    def lambda_744A():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_744A)

    Sleep(30)

    @scena.Lambda('lambda_746A')
    def lambda_746A():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_746A)

    @scena.Lambda('lambda_7485')
    def lambda_7485():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7485)

    Sleep(60)

    @scena.Lambda('lambda_74A5')
    def lambda_74A5():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_74A5)

    @scena.Lambda('lambda_74C0')
    def lambda_74C0():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_74C0)

    Sleep(70)

    @scena.Lambda('lambda_74E0')
    def lambda_74E0():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_74E0)

    @scena.Lambda('lambda_74FB')
    def lambda_74FB():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_74FB)

    Return()

# id: 0x0010 offset: 0x7511
@scena.Code('func_10_7511')
def func_10_7511():
    @scena.Lambda('lambda_7517')
    def lambda_7517():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005D, 0x0001, lambda_7517)

    @scena.Lambda('lambda_7532')
    def lambda_7532():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005F, 0x0001, lambda_7532)

    Sleep(100)

    @scena.Lambda('lambda_7552')
    def lambda_7552():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005E, 0x0001, lambda_7552)

    Sleep(80)

    @scena.Lambda('lambda_7572')
    def lambda_7572():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0060, 0x0001, lambda_7572)

    @scena.Lambda('lambda_758D')
    def lambda_758D():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0062, 0x0001, lambda_758D)

    Sleep(70)

    @scena.Lambda('lambda_75AD')
    def lambda_75AD():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0061, 0x0001, lambda_75AD)

    Sleep(30)

    @scena.Lambda('lambda_75CD')
    def lambda_75CD():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005B, 0x0001, lambda_75CD)

    Sleep(90)

    @scena.Lambda('lambda_75ED')
    def lambda_75ED():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0058, 0x0001, lambda_75ED)

    @scena.Lambda('lambda_7608')
    def lambda_7608():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005C, 0x0001, lambda_7608)

    @scena.Lambda('lambda_7623')
    def lambda_7623():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0059, 0x0001, lambda_7623)

    Sleep(40)

    @scena.Lambda('lambda_7643')
    def lambda_7643():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0057, 0x0001, lambda_7643)

    @scena.Lambda('lambda_765E')
    def lambda_765E():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005A, 0x0001, lambda_765E)

    Sleep(30)

    @scena.Lambda('lambda_767E')
    def lambda_767E():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0051, 0x0001, lambda_767E)

    @scena.Lambda('lambda_7699')
    def lambda_7699():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0054, 0x0001, lambda_7699)

    Sleep(70)

    @scena.Lambda('lambda_76B9')
    def lambda_76B9():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0053, 0x0001, lambda_76B9)

    @scena.Lambda('lambda_76D4')
    def lambda_76D4():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0055, 0x0001, lambda_76D4)

    Sleep(40)

    @scena.Lambda('lambda_76F4')
    def lambda_76F4():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0052, 0x0001, lambda_76F4)

    @scena.Lambda('lambda_770F')
    def lambda_770F():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0056, 0x0001, lambda_770F)

    @scena.Lambda('lambda_772A')
    def lambda_772A():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004F, 0x0001, lambda_772A)

    Sleep(50)

    @scena.Lambda('lambda_774A')
    def lambda_774A():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004B, 0x0001, lambda_774A)

    @scena.Lambda('lambda_7765')
    def lambda_7765():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004E, 0x0001, lambda_7765)

    Sleep(30)

    @scena.Lambda('lambda_7785')
    def lambda_7785():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004D, 0x0001, lambda_7785)

    Sleep(100)

    @scena.Lambda('lambda_77A5')
    def lambda_77A5():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004C, 0x0001, lambda_77A5)

    @scena.Lambda('lambda_77C0')
    def lambda_77C0():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0050, 0x0001, lambda_77C0)

    Sleep(30)

    @scena.Lambda('lambda_77E0')
    def lambda_77E0():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004A, 0x0001, lambda_77E0)

    @scena.Lambda('lambda_77FB')
    def lambda_77FB():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0047, 0x0001, lambda_77FB)

    Sleep(60)

    @scena.Lambda('lambda_781B')
    def lambda_781B():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0045, 0x0001, lambda_781B)

    @scena.Lambda('lambda_7836')
    def lambda_7836():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0001, lambda_7836)

    Sleep(70)

    @scena.Lambda('lambda_7856')
    def lambda_7856():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_7856)

    @scena.Lambda('lambda_7871')
    def lambda_7871():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0001, lambda_7871)

    Return()

# id: 0x0011 offset: 0x7887
@scena.Code('func_11_7887')
def func_11_7887():
    @scena.Lambda('lambda_788D')
    def lambda_788D():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007B, 0x0001, lambda_788D)

    @scena.Lambda('lambda_78A8')
    def lambda_78A8():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007D, 0x0001, lambda_78A8)

    Sleep(100)

    @scena.Lambda('lambda_78C8')
    def lambda_78C8():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007C, 0x0001, lambda_78C8)

    Sleep(80)

    @scena.Lambda('lambda_78E8')
    def lambda_78E8():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007E, 0x0001, lambda_78E8)

    @scena.Lambda('lambda_7903')
    def lambda_7903():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_7903)

    Sleep(70)

    @scena.Lambda('lambda_7923')
    def lambda_7923():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_7923)

    Sleep(30)

    @scena.Lambda('lambda_7943')
    def lambda_7943():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0079, 0x0001, lambda_7943)

    Sleep(90)

    @scena.Lambda('lambda_7963')
    def lambda_7963():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0076, 0x0001, lambda_7963)

    @scena.Lambda('lambda_797E')
    def lambda_797E():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007A, 0x0001, lambda_797E)

    @scena.Lambda('lambda_7999')
    def lambda_7999():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0077, 0x0001, lambda_7999)

    Sleep(40)

    @scena.Lambda('lambda_79B9')
    def lambda_79B9():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0075, 0x0001, lambda_79B9)

    @scena.Lambda('lambda_79D4')
    def lambda_79D4():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0078, 0x0001, lambda_79D4)

    Sleep(30)

    @scena.Lambda('lambda_79F4')
    def lambda_79F4():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006F, 0x0001, lambda_79F4)

    @scena.Lambda('lambda_7A0F')
    def lambda_7A0F():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0072, 0x0001, lambda_7A0F)

    Sleep(70)

    @scena.Lambda('lambda_7A2F')
    def lambda_7A2F():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0071, 0x0001, lambda_7A2F)

    @scena.Lambda('lambda_7A4A')
    def lambda_7A4A():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0073, 0x0001, lambda_7A4A)

    Sleep(40)

    @scena.Lambda('lambda_7A6A')
    def lambda_7A6A():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0070, 0x0001, lambda_7A6A)

    @scena.Lambda('lambda_7A85')
    def lambda_7A85():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0074, 0x0001, lambda_7A85)

    @scena.Lambda('lambda_7AA0')
    def lambda_7AA0():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006D, 0x0001, lambda_7AA0)

    Sleep(50)

    @scena.Lambda('lambda_7AC0')
    def lambda_7AC0():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0069, 0x0001, lambda_7AC0)

    @scena.Lambda('lambda_7ADB')
    def lambda_7ADB():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006C, 0x0001, lambda_7ADB)

    Sleep(30)

    @scena.Lambda('lambda_7AFB')
    def lambda_7AFB():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006B, 0x0001, lambda_7AFB)

    Sleep(100)

    @scena.Lambda('lambda_7B1B')
    def lambda_7B1B():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006A, 0x0001, lambda_7B1B)

    @scena.Lambda('lambda_7B36')
    def lambda_7B36():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006E, 0x0001, lambda_7B36)

    Sleep(30)

    @scena.Lambda('lambda_7B56')
    def lambda_7B56():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0068, 0x0001, lambda_7B56)

    @scena.Lambda('lambda_7B71')
    def lambda_7B71():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0065, 0x0001, lambda_7B71)

    Sleep(60)

    @scena.Lambda('lambda_7B91')
    def lambda_7B91():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0063, 0x0001, lambda_7B91)

    @scena.Lambda('lambda_7BAC')
    def lambda_7BAC():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0066, 0x0001, lambda_7BAC)

    Sleep(70)

    @scena.Lambda('lambda_7BCC')
    def lambda_7BCC():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0064, 0x0001, lambda_7BCC)

    @scena.Lambda('lambda_7BE7')
    def lambda_7BE7():
        OP_91(0x00FE, 0, 0, 34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0067, 0x0001, lambda_7BE7)

    Return()

# id: 0x0012 offset: 0x7BFD
@scena.Code('func_12_7BFD')
def func_12_7BFD():
    OP_24(0x010F, 0x5F)
    OP_24(0x0110, 0x5A)
    Sleep(350)

    OP_24(0x010F, 0x5A)
    OP_24(0x0110, 0x55)
    Sleep(350)

    OP_24(0x010F, 0x55)
    OP_24(0x0110, 0x50)
    Sleep(350)

    OP_24(0x010F, 0x50)
    OP_24(0x0110, 0x4B)
    Sleep(350)

    OP_24(0x010F, 0x4B)
    OP_24(0x0110, 0x46)
    Sleep(350)

    OP_24(0x010F, 0x46)
    OP_24(0x0110, 0x41)
    Sleep(350)

    OP_24(0x010F, 0x41)
    OP_24(0x0110, 0x3C)
    Sleep(350)

    OP_24(0x010F, 0x3C)
    OP_24(0x0110, 0x37)
    Sleep(350)

    OP_24(0x010F, 0x37)
    OP_24(0x0110, 0x32)
    Sleep(350)

    OP_24(0x010F, 0x32)
    OP_24(0x0110, 0x2D)
    Sleep(350)

    OP_24(0x010F, 0x2D)
    OP_24(0x0110, 0x28)
    Sleep(350)

    OP_24(0x010F, 0x28)
    OP_24(0x0110, 0x23)
    Sleep(350)

    OP_24(0x010F, 0x23)
    OP_24(0x0110, 0x1E)
    Sleep(350)

    OP_23(0x010F)
    OP_23(0x0110)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
