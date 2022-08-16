import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4204_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4204   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4204.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT06/CH20153._CH', 'ED6_DT06/CH20153P._CP'),
        ('ED6_DT06/CH20154._CH', 'ED6_DT06/CH20154P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xE2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xE2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xE2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xE2
@scena.Code('Init')
def Init():
    Event(0, func_02_E8)

    Return()

# id: 0x0001 offset: 0xE7
@scena.Code('func_01_E7')
def func_01_E7():
    Return()

# id: 0x0002 offset: 0xE8
@scena.Code('func_02_E8')
def func_02_E8():
    EventBegin(0x00)
    OP_77(0xFF, 0xA0, 0x46, 0x00, 0x00000000)
    OP_20(0x00000000)
    CameraMove(-42280, 16000, 81720, 0)
    OP_67(0, 5390, -10000, 0)
    CameraSetDistance(1470, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)
    ChrClearFlags(0x0008, 0x0002)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -42780, 16000, 81000, 90)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0101, -41300, 16000, 81000, 0)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetSubChip(0x0101, 5)
    FadeIn(1000, 0)
    Sleep(1250)

    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0020141442V#594F我的艾丝蒂尔……\n',
            '如太阳般耀眼的你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190143V和你在一起的时光虽然幸福\n',
            '同时，却也非常痛苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190144V因为就像明亮的光芒会投下浓重的阴影……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190145V与你在一起相处得越久\n',
            '我，也对自己令人憎恶的本性\n',
            '认识得更加深刻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190146V所以，我甚至想过，\n',
            '要是当初没遇见你该多好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x07, 0x09, 800)
    Sleep(400)

    @scena.Lambda('lambda_02D8')
    def lambda_02D8():
        CameraMove(-41280, 16000, 81720, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_02D8)

    ChrMoveTo(0x0008, -42000, 16000, 81100, 1000, 0x00)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetFlags(0x0008, 0x0002)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_99(0x0008, 0x00, 0x02, 1200)
    Sleep(2000)

    FadeOut(1500, 0, -1)
    OP_0D()
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x0101, 0x0002)
    NewScene('ED6_DT21/E0001._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
