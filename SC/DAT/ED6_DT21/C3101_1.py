import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3101_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3101_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C3101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x326B
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
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x0011, 14430, 0, 26280, 90)
    SetChrPos(0x0012, 14430, 0, 24350, 90)
    SetChrPos(0x0013, 14430, 0, 22420, 90)
    SetChrPos(0x0014, 14430, 0, 20490, 90)
    SetChrPos(0x0015, 14430, 0, 18560, 90)
    SetChrPos(0x0016, 14430, 0, 16630, 90)
    SetChrPos(0x0017, 17760, 0, 26280, 270)
    SetChrPos(0x0018, 17760, 0, 24350, 270)
    SetChrPos(0x0019, 17760, 0, 22420, 270)
    SetChrPos(0x001A, 17760, 0, 20490, 270)
    SetChrPos(0x001B, 17760, 0, 18560, 270)
    SetChrPos(0x001C, 17760, 0, 16630, 270)
    SetChrChipByIndex(0x0011, 9)
    SetChrChipByIndex(0x0012, 9)
    SetChrChipByIndex(0x0013, 9)
    SetChrChipByIndex(0x0014, 9)
    SetChrChipByIndex(0x0015, 9)
    SetChrChipByIndex(0x0016, 9)
    SetChrChipByIndex(0x0017, 9)
    SetChrChipByIndex(0x0018, 9)
    SetChrChipByIndex(0x0019, 9)
    SetChrChipByIndex(0x001A, 9)
    SetChrChipByIndex(0x001B, 9)
    SetChrChipByIndex(0x001C, 9)
    SetChrPos(0x0101, 300, 0, 23270, 90)
    SetChrPos(0x00F7, -500, 0, 21820, 90)
    SetChrPos(0x0104, -1800, 0, 23140, 90)
    SetChrPos(0x0105, -2000, 0, 21900, 90)
    SetChrPos(0x000D, -11810, 0, 24790, 90)
    SetChrPos(0x000E, -11110, 0, 23590, 90)
    SetChrPos(0x000F, -12010, 0, 22390, 90)
    SetChrPos(0x0010, -11310, 0, 21190, 90)
    ClearChrFlags(0x0026, 0x0080)
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
    ClearChrFlags(0x0045, 0x0080)
    ClearChrFlags(0x0046, 0x0080)
    ClearChrFlags(0x0047, 0x0080)
    SetChrPos(0x0046, -11000, 0, 28500, 90)
    SetChrPos(0x0026, -12000, 0, 28000, 90)
    SetChrPos(0x0027, -13000, 0, 28000, 90)
    SetChrPos(0x0028, -14000, 0, 28000, 90)
    SetChrPos(0x0029, -15000, 0, 28000, 90)
    SetChrPos(0x002A, -16000, 0, 28000, 90)
    SetChrPos(0x002B, -17000, 0, 28000, 90)
    SetChrPos(0x002C, -18000, 0, 28000, 90)
    SetChrPos(0x002D, -19000, 0, 28000, 90)
    SetChrPos(0x002E, -12000, 0, 29000, 90)
    SetChrPos(0x002F, -13000, 0, 29000, 90)
    SetChrPos(0x0030, -14000, 0, 29000, 90)
    SetChrPos(0x0031, -15000, 0, 29000, 90)
    SetChrPos(0x0032, -16000, 0, 29000, 90)
    SetChrPos(0x0033, -17000, 0, 29000, 90)
    SetChrPos(0x0034, -18000, 0, 29000, 90)
    SetChrPos(0x0035, -19000, 0, 29000, 90)
    SetChrPos(0x0047, 0, 0, 28500, 90)
    SetChrPos(0x0036, -8000, 0, 28000, 90)
    SetChrPos(0x0037, -7000, 0, 28000, 90)
    SetChrPos(0x0038, -6000, 0, 28000, 90)
    SetChrPos(0x0039, -5000, 0, 28000, 90)
    SetChrPos(0x003A, -4000, 0, 28000, 90)
    SetChrPos(0x003B, -3000, 0, 28000, 90)
    SetChrPos(0x003C, -2000, 0, 28000, 90)
    SetChrPos(0x003D, -1000, 0, 28000, 90)
    SetChrPos(0x003E, -8000, 0, 29000, 90)
    SetChrPos(0x003F, -7000, 0, 29000, 90)
    SetChrPos(0x0040, -6000, 0, 29000, 90)
    SetChrPos(0x0041, -5000, 0, 29000, 90)
    SetChrPos(0x0042, -4000, 0, 29000, 90)
    SetChrPos(0x0043, -3000, 0, 29000, 90)
    SetChrPos(0x0044, -2000, 0, 29000, 90)
    SetChrPos(0x0045, -1000, 0, 29000, 90)
    OP_6D(23710, 0, 24140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3830, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    CreateThread(0x0011, 0x01, 0x00, 0x0004)
    CreateThread(0x0017, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0012, 0x01, 0x00, 0x0004)
    CreateThread(0x0018, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0013, 0x01, 0x00, 0x0004)
    CreateThread(0x0019, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0014, 0x01, 0x00, 0x0004)
    CreateThread(0x001A, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0015, 0x01, 0x00, 0x0004)
    CreateThread(0x001B, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0016, 0x01, 0x00, 0x0004)
    CreateThread(0x001C, 0x01, 0x00, 0x0004)
    CreateThread(0x0047, 0x01, 0x01, 0x000A)
    CreateThread(0x0036, 0x01, 0x01, 0x000C)
    CreateThread(0x0037, 0x01, 0x01, 0x000C)
    CreateThread(0x0038, 0x01, 0x01, 0x000C)
    CreateThread(0x0039, 0x01, 0x01, 0x000C)
    CreateThread(0x003A, 0x01, 0x01, 0x000C)
    CreateThread(0x003B, 0x01, 0x01, 0x000C)
    CreateThread(0x003C, 0x01, 0x01, 0x000C)
    CreateThread(0x003D, 0x01, 0x01, 0x000C)
    CreateThread(0x003E, 0x01, 0x01, 0x000C)
    CreateThread(0x003F, 0x01, 0x01, 0x000C)
    CreateThread(0x0040, 0x01, 0x01, 0x000C)
    CreateThread(0x0041, 0x01, 0x01, 0x000C)
    CreateThread(0x0042, 0x01, 0x01, 0x000C)
    CreateThread(0x0043, 0x01, 0x01, 0x000C)
    CreateThread(0x0044, 0x01, 0x01, 0x000C)
    CreateThread(0x0045, 0x01, 0x01, 0x000C)
    Sleep(1000)

    CreateThread(0x0046, 0x01, 0x01, 0x0009)
    CreateThread(0x0026, 0x01, 0x01, 0x000B)
    CreateThread(0x0027, 0x01, 0x01, 0x000B)
    CreateThread(0x0028, 0x01, 0x01, 0x000B)
    CreateThread(0x0029, 0x01, 0x01, 0x000B)
    CreateThread(0x002A, 0x01, 0x01, 0x000B)
    CreateThread(0x002B, 0x01, 0x01, 0x000B)
    CreateThread(0x002C, 0x01, 0x01, 0x000B)
    CreateThread(0x002D, 0x01, 0x01, 0x000B)
    CreateThread(0x002E, 0x01, 0x01, 0x000B)
    CreateThread(0x002F, 0x01, 0x01, 0x000B)
    CreateThread(0x0030, 0x01, 0x01, 0x000B)
    CreateThread(0x0031, 0x01, 0x01, 0x000B)
    CreateThread(0x0032, 0x01, 0x01, 0x000B)
    CreateThread(0x0033, 0x01, 0x01, 0x000B)
    CreateThread(0x0034, 0x01, 0x01, 0x000B)
    CreateThread(0x0035, 0x01, 0x01, 0x000B)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0718')
    def lambda_0718():
        OP_6D(-5110, 0, 27310, 8000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0718)

    @scena.Lambda('lambda_0730')
    def lambda_0730():
        OP_6B(3700, 8000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0730)

    @scena.Lambda('lambda_0740')
    def lambda_0740():
        OP_6C(30000, 8000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0740)

    Sleep(2000)

    @scena.Lambda('lambda_0755')
    def lambda_0755():
        OP_8E(0x0101, 9500, 0, 23270, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0755)

    @scena.Lambda('lambda_0770')
    def lambda_0770():
        OP_8E(0x00F7, 8800, 0, 21820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0770)

    @scena.Lambda('lambda_078B')
    def lambda_078B():
        OP_8E(0x0104, 7800, 0, 23140, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_078B)

    @scena.Lambda('lambda_07A6')
    def lambda_07A6():
        OP_8E(0x0105, 7400, 0, 21900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_07A6)

    Sleep(5000)

    OP_0D()
    Fade(1000)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000B, 0x02)
    OP_6D(9500, 0, 23270, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010450094V#1016F啊～感觉好怀念啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_894',
    )

    OP_61(0x0106)

    ChrTalk(
        0x0106,
        (
            '#0050450095V#051F嗯，自从那次之后就再也没有过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_894(): pass

    label('loc_894')

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450096V#1015F上次来的时候因为天色暗\n',
            '看不太清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450097V#1011F现在这么一看，\n',
            '这个基地还真是很大呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_960',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030450098V#020F真的呢……\n',
            '和要塞这个称呼是很相称。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_960(): pass

    label('loc_960')

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060450099V#040F嗯，因为这里是\n',
            '王国军的大本营。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450100V所以与各地的要塞关所\n',
            '在规模上稍有差别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0104, 270, 400)
    OP_62(0x0104, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0104)

    ChrTalk(
        0x0104,
        (
            '#0040450101V#030F哎哟，看来快要\n',
            '开始了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x000D, 30)
    SetChrChipByIndex(0x000E, 30)
    SetChrChipByIndex(0x000F, 30)
    SetChrChipByIndex(0x0010, 30)

    @scena.Lambda('lambda_0A51')
    def lambda_0A51():
        OP_8C(0x00F7, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0A51)

    Sleep(250)

    @scena.Lambda('lambda_0A64')
    def lambda_0A64():
        OP_8C(0x0101, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A64)

    Sleep(150)

    @scena.Lambda('lambda_0A77')
    def lambda_0A77():
        OP_8C(0x0105, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0A77)

    @scena.Lambda('lambda_0A85')
    def lambda_0A85():
        OP_8E(0x000D, -3450, 0, 24790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0A85)

    @scena.Lambda('lambda_0AA0')
    def lambda_0AA0():
        OP_8E(0x000E, -3450, 0, 23590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0AA0)

    @scena.Lambda('lambda_0ABB')
    def lambda_0ABB():
        OP_8E(0x000F, -3450, 0, 22390, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0ABB)

    @scena.Lambda('lambda_0AD6')
    def lambda_0AD6():
        OP_8E(0x0010, -3450, 0, 21190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0AD6)

    @scena.Lambda('lambda_0AF1')
    def lambda_0AF1():
        OP_6D(0, 0, 24840, 3000)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_0AF1)

    @scena.Lambda('lambda_0B09')
    def lambda_0B09():
        OP_67(0, 8119, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_0B09)

    @scena.Lambda('lambda_0B21')
    def lambda_0B21():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0025, 0x0003, lambda_0B21)

    @scena.Lambda('lambda_0B31')
    def lambda_0B31():
        OP_6B(2970, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B31)

    WaitForThreadExit(0x0025, 0x0001)
    WaitForThreadExit(0x0025, 0x0002)
    WaitForThreadExit(0x0025, 0x0003)
    WaitForThreadExit(0x000B, 0x0001)
    Sleep(1500)

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 0, 0, 32750, 180)
    SetChrPos(0x0101, 8500, 0, 23000, 270)
    SetChrPos(0x00F7, 9500, 0, 24250, 270)
    SetChrPos(0x0104, 9500, 0, 21750, 270)
    SetChrPos(0x0105, 10500, 0, 23000, 270)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)

    @scena.Lambda('lambda_0BF0')
    def lambda_0BF0():
        OP_94(0x01, 0x0000, 0x0000, 0x000015E0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0BF0)

    Sleep(50)

    @scena.Lambda('lambda_0C0B')
    def lambda_0C0B():
        OP_94(0x01, 0x0001, 0x0000, 0x000015E0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0C0B)

    Sleep(100)

    @scena.Lambda('lambda_0C26')
    def lambda_0C26():
        OP_94(0x01, 0x0002, 0x0000, 0x000015E0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0C26)

    Sleep(50)

    @scena.Lambda('lambda_0C41')
    def lambda_0C41():
        OP_94(0x01, 0x0003, 0x0000, 0x000015E0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0C41)

    OP_8E(0x000B, 0, 0, 26140, 2000, 0x00)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0620450102V#700F那么现在开始\n',
            '进行模拟战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450103V这次特别邀请到游击士协会的\n',
            '精锐来担任对抗部队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450104V希望各位官兵能尽全力挑战。\n',
            '其中可是包含了武术大赛冠军的强手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x00, 0x01, 0x0005)
    CreateThread(0x000E, 0x00, 0x01, 0x0006)
    CreateThread(0x000F, 0x00, 0x01, 0x0007)
    CreateThread(0x0010, 0x00, 0x01, 0x0008)

    ChrTalk(
        0x000D,
        (
            '#2450450105V#2P冠、冠军……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2470450106V#3P这、这可难对付了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450107V#700F和刚才说明过的一样，\n',
            '预计需要诸位进行二连战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450108V请牢记这一点\n',
            '来进行战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450109V#1006F#3P嗯，明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x0010, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_E9E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450110V#050F#2P几连战都没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450111V赶快开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_E9E(): pass

    label('loc_E9E')

    ChrTalk(
        0x0103,
        (
            '#0030450112V#525F#2P呵呵，几连战都没关系哦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450113V我们会奉陪到底的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EF0(): pass

    label('loc_EF0')

    OP_8C(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450114V#700F#5P好，那就开始吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450115V──双方预备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x01, 0x000D)
    CreateThread(0x000E, 0x01, 0x01, 0x000E)
    CreateThread(0x000F, 0x01, 0x01, 0x000F)
    CreateThread(0x0010, 0x01, 0x01, 0x0010)
    OP_8C(0x0101, 270, 400)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    Fade(1000)
    SetChrChipByIndex(0x0104, 15)
    SetChrChipByIndex(0x0101, 11)
    SetChrChipByIndex(0x0105, 17)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_F97',
    )

    SetChrChipByIndex(0x00F7, 19)

    Jump('loc_F9C')

    def _loc_F97(): pass

    label('loc_F97')

    SetChrChipByIndex(0x00F7, 13)

    def _loc_F9C(): pass

    label('loc_F9C')

    SetChrChipByIndex(0x000D, 21)
    SetChrChipByIndex(0x000E, 21)
    SetChrChipByIndex(0x000F, 21)
    SetChrChipByIndex(0x0010, 21)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0620450116V#704F#5P#3S比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x8C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000C80, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_FFE'),
        (0x00000001, 'loc_1005'),
        (-1, 'loc_100C'),
    )

    def _loc_FFE(): pass

    label('loc_FFE')

    Call(1, 0x0001)

    Jump('loc_100C')

    def _loc_1005(): pass

    label('loc_1005')

    Call(1, 0x0004)

    Jump('loc_100C')

    def _loc_100C(): pass

    label('loc_100C')

    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x100F
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6C(0, 0)
    OP_6B(2970, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0104, 15)
    SetChrChipByIndex(0x0101, 11)
    SetChrChipByIndex(0x0105, 17)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1085',
    )

    SetChrChipByIndex(0x00F7, 19)

    Jump('loc_108A')

    def _loc_1085(): pass

    label('loc_1085')

    SetChrChipByIndex(0x00F7, 13)

    def _loc_108A(): pass

    label('loc_108A')

    SetChrPos(0x0101, 2900, 0, 23000, 270)
    SetChrPos(0x00F7, 3900, 0, 24250, 270)
    SetChrPos(0x0104, 3900, 0, 21750, 270)
    SetChrPos(0x0105, 4900, 0, 23000, 270)
    SetChrPos(0x000D, -3900, 0, 24250, 90)
    SetChrPos(0x000E, -2900, 0, 23000, 90)
    SetChrPos(0x000F, -4900, 0, 23000, 90)
    SetChrPos(0x0010, -3900, 0, 21750, 90)
    SetChrChipByIndex(0x000D, 22)
    SetChrChipByIndex(0x000E, 22)
    SetChrChipByIndex(0x000F, 22)
    SetChrChipByIndex(0x0010, 22)
    SetChrSubChip(0x000D, 3)
    SetChrSubChip(0x000E, 3)
    SetChrSubChip(0x000F, 3)
    SetChrSubChip(0x0010, 3)
    SetChrPos(0x000B, 0, 0, 26140, 180)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0620450117V#700F──到此为止！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450118V#1006F#3P好，赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_11CB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450119V#051F#2P果然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11F1')

    def _loc_11CB(): pass

    label('loc_11CB')

    ChrTalk(
        0x0103,
        (
            '#0030450120V#027F#2P果然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11F1(): pass

    label('loc_11F1')

    ChrTalk(
        0x0105,
        (
            '#0060450121V#040F……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    OP_99(0x000E, 0x03, 0x00, 0x000007D0)

    ChrTalk(
        0x000E,
        (
            '#2460450122V#4P啊，好痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1259')
    def lambda_1259():
        ChrTurnDirection(0x000B, 0x000E, 400)
        Yield()

        Jump('lambda_1259')

    DispatchAsync2(0x000B, 0x0001, lambda_1259)

    ChrTalk(
        0x000B,
        (
            '#0620450123V#700F你们在发什么呆？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450124V立即撤离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2460450125V#4P是、是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x01, 0x0011)
    Sleep(100)

    CreateThread(0x000F, 0x01, 0x01, 0x0011)
    Sleep(50)

    CreateThread(0x0010, 0x01, 0x01, 0x0011)
    OP_8C(0x000E, 270, 0)
    SetChrChipByIndex(0x000E, 10)

    @scena.Lambda('lambda_12F1')
    def lambda_12F1():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001F40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_12F1)

    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    SetChrFlags(0x000E, 0x0080)
    TerminateThread(0x000B, 0x01)

    ChrTalk(
        0x000B,
        (
            '#0620450126V#704F──接下来，贝尔克副队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_134B')
    def lambda_134B():
        ChrTurnDirection(0x000B, 0x0025, 0)
        Yield()

        Jump('lambda_134B')

    DispatchAsync2(0x000B, 0x0001, lambda_134B)

    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0025, 31)
    SetChrPos(0x000D, -10000, 0, 23000, 90)
    SetChrPos(0x0025, -12000, 0, 23000, 90)
    SetChrPos(0x000F, -11110, 0, 24250, 90)
    SetChrPos(0x0010, -11110, 0, 21750, 90)

    ChrTalk(
        0x0025,
        (
            '#3170450127V#2P在！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13D2')
    def lambda_13D2():
        OP_94(0x01, 0x000D, 0x0000, 0x00001BBC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_13D2)

    @scena.Lambda('lambda_13E8')
    def lambda_13E8():
        OP_94(0x01, 0x0025, 0x0000, 0x00001BBC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_13E8)

    @scena.Lambda('lambda_13FE')
    def lambda_13FE():
        OP_94(0x01, 0x000F, 0x0000, 0x00001BBC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_13FE)

    @scena.Lambda('lambda_1414')
    def lambda_1414():
        OP_94(0x01, 0x0010, 0x0000, 0x00001BBC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1414)

    WaitForThreadExit(0x0025, 0x0001)
    SetChrChipByIndex(0x0025, 23)
    SetChrChipByIndex(0x000D, 21)
    SetChrChipByIndex(0x000F, 21)
    SetChrChipByIndex(0x0010, 21)
    Sleep(1000)

    TerminateThread(0x000B, 0x01)
    OP_8C(0x000B, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450128V#1007F#3P看、看来真的\n',
            '不打算让我们休息了 。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0104, 0x01, 0x01, 0x0012)

    ChrTalk(
        0x0104,
        (
            '#0040450129V#035F#3P呼，真是服了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450130V至少让我整理一下\n',
            '乱了的头发也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3170450131V#4P嗯，不愧是大赛冠军……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3170450132V#4P故意露出破绽，\n',
            '打算是想让我们掉以轻心吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010450133V#1019F#3P不……你错了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450134V这、这绝对是你\n',
            '想得太多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620450135V#700F#5P现在还在训练中啊。\n',
            '不要窃窃私语。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450136V那么第２战──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450137V#704F#3S──比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Battle(0x00000C81, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1659'),
        (0x00000001, 'loc_1660'),
        (-1, 'loc_1667'),
    )

    def _loc_1659(): pass

    label('loc_1659')

    Call(1, 0x0002)

    Jump('loc_1667')

    def _loc_1660(): pass

    label('loc_1660')

    Call(1, 0x0004)

    Jump('loc_1667')

    def _loc_1667(): pass

    label('loc_1667')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x166A
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6C(0, 0)
    OP_6B(2970, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0104, 15)
    SetChrChipByIndex(0x0101, 11)
    SetChrChipByIndex(0x0105, 17)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_16E5',
    )

    SetChrChipByIndex(0x00F7, 19)

    Jump('loc_16EA')

    def _loc_16E5(): pass

    label('loc_16E5')

    SetChrChipByIndex(0x00F7, 13)

    def _loc_16EA(): pass

    label('loc_16EA')

    SetChrPos(0x0101, 2900, 0, 23000, 270)
    SetChrPos(0x00F7, 3900, 0, 24250, 270)
    SetChrPos(0x0104, 3900, 0, 21750, 270)
    SetChrPos(0x0105, 4900, 0, 23000, 270)
    SetChrPos(0x000D, -3900, 0, 24250, 90)
    SetChrPos(0x000F, -2900, 0, 23000, 90)
    SetChrPos(0x0025, -4900, 0, 23000, 90)
    SetChrPos(0x0010, -3900, 0, 21750, 90)
    SetChrPos(0x000B, 0, 0, 26140, 180)
    SetChrChipByIndex(0x000D, 22)
    SetChrChipByIndex(0x0025, 24)
    SetChrChipByIndex(0x000F, 22)
    SetChrChipByIndex(0x0010, 22)
    SetChrSubChip(0x000D, 3)
    SetChrSubChip(0x0025, 3)
    SetChrSubChip(0x000F, 3)
    SetChrSubChip(0x0010, 3)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0620450138V#704F#5P──到此为止！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x00F7, 65535)
    SetChrChipByIndex(0x0105, 65535)
    SetChrChipByIndex(0x0104, 65535)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040450139V#030F#3P呼，我们赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450140V#1002F#3P嗯，好不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0025, 0x03, 0x00, 0x000007D0)

    ChrTalk(
        0x0025,
        (
            '#3170450141V#4P唔……输了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0025, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450142V#700F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450143V副队长……\n',
            '还挺得住吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0025, 0x000B, 400)

    ChrTalk(
        0x0025,
        (
            '#3170450144V#4P……………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0025, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0025,
        (
            '#3170450145V#4P是、是的！　没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620450146V#703F很好……\n',
            '那么马上做准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3170450147V#4P了解！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x01, 0x0011)
    Sleep(100)

    CreateThread(0x000F, 0x01, 0x01, 0x0011)
    Sleep(50)

    CreateThread(0x0010, 0x01, 0x01, 0x0011)
    OP_8C(0x0025, 270, 0)
    SetChrChipByIndex(0x0025, 31)

    @scena.Lambda('lambda_19AB')
    def lambda_19AB():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001F40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_19AB)

    Sleep(1000)

    @scena.Lambda('lambda_19C6')
    def lambda_19C6():
        OP_8C(0x0101, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19C6)

    @scena.Lambda('lambda_19D4')
    def lambda_19D4():
        OP_8C(0x00F7, 315, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_19D4)

    @scena.Lambda('lambda_19E2')
    def lambda_19E2():
        OP_8C(0x0104, 315, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_19E2)

    @scena.Lambda('lambda_19F0')
    def lambda_19F0():
        OP_8C(0x0105, 315, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_19F0)

    OP_66(0x0000)
    OP_6D(2400, 0, 24430, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010450148V#1015F#3P请问，所谓的准备是指……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450149V#030F#3P呵呵，让我猜猜看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450150V是不是被我华丽的战斗所感动，\n',
            '而要为我开设庆功宴呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450151V#702F#1P庆功宴……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450152V#1002F#3P……请你不要理他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620450153V#703F#1P了、了解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450154V#700F不，准备当然指的是\n',
            '下一场模拟战斗的准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010450155V#1004F#3P不、不是吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450156V你一开始不是说\n',
            '『二连战』吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1D16',
    )

    ChrTalk(
        0x000B,
        (
            '#0620450157V#700F#1P嗯， 确实这么说过──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450158V不过，你们是这样回答的：\n',
            '『几连战都没关系』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050450159V#552F#2P切……\n',
            '居然被你记牢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450160V#1009F#3P阿、阿加特～～\n',
            '为什么这么多嘴！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050450161V#551F#1P嗯，别介意。\n',
            '只是一时脱口而出罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E3A')

    def _loc_1D16(): pass

    label('loc_1D16')

    ChrTalk(
        0x000B,
        (
            '#0620450157V#700F#1P嗯， 确实这么说过──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450163V不过，你们是这样回答的：\n',
            '『几连战都没关系』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030450164V#023F#2P哎呀，你记得真牢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450165V#1007F#3P雪、雪拉姐～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030450166V#025F#2P看、看来是没办法了。\n',
            '谁让当时脱口而出说了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E3A(): pass

    label('loc_1E3A')

    ChrTalk(
        0x000B,
        (
            '#0620450167V#700F#1P那就满足你们的要求，\n',
            '再较量一场吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450168V就由我亲自来担任──\n',
            '你们最后的一个对手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450169V#1004F#3P希、希德中校！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450170V#031F#3P呵呵，总算\n',
            '露出你真正的想法了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450171V是不是手痒了，迫不及待地要较量一番啊──\n',
            '有话就直说嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620450172V#701F#1P哈哈，被你看穿了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1FEE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450173V#051F#2P哼，果不其然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450174V正好，我也正想和你比试一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_204D')

    def _loc_1FEE(): pass

    label('loc_1FEE')

    ChrTalk(
        0x0103,
        (
            '#0030450175V#027F#2P呵呵，果然如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450176V#525F不过，我并不讨厌你的这种想法哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_204D(): pass

    label('loc_204D')

    WaitForThreadExit(0x0010, 0x0001)
    SetChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0025, 31)
    SetChrChipByIndex(0x000F, 10)
    SetChrChipByIndex(0x0010, 10)
    SetChrPos(0x0025, -10000, 0, 23000, 90)
    SetChrPos(0x000F, -9110, 0, 24250, 90)
    SetChrPos(0x0010, -9110, 0, 21750, 90)

    @scena.Lambda('lambda_20AE')
    def lambda_20AE():
        OP_6D(0, 0, 24840, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_20AE)

    @scena.Lambda('lambda_20C6')
    def lambda_20C6():
        OP_94(0x01, 0x0025, 0x0000, 0x000013EC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_20C6)

    @scena.Lambda('lambda_20DC')
    def lambda_20DC():
        OP_94(0x01, 0x000F, 0x0000, 0x000013EC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_20DC)

    @scena.Lambda('lambda_20F2')
    def lambda_20F2():
        OP_94(0x01, 0x0010, 0x0000, 0x000013EC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_20F2)

    WaitForThreadExit(0x0025, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    OP_66(0x0001)
    SetChrChipByIndex(0x0025, 23)
    SetChrChipByIndex(0x000F, 21)
    SetChrChipByIndex(0x0010, 21)

    ChrTalk(
        0x0025,
        (
            '#3170450177V#4P让您久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0025, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450178V#700F辛苦你了────',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2173')
    def lambda_2173():
        OP_67(0, 19910, -29700, 2000)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_2173)

    @scena.Lambda('lambda_218B')
    def lambda_218B():
        OP_6B(1000, 2000)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_218B)

    @scena.Lambda('lambda_219B')
    def lambda_219B():
        ChrTurnDirection(0x0101, 0x000B, 0)
        Yield()

        Jump('lambda_219B')

    DispatchAsync2(0x0101, 0x0001, lambda_219B)

    @scena.Lambda('lambda_21AC')
    def lambda_21AC():
        ChrTurnDirection(0x00F7, 0x000B, 0)
        Yield()

        Jump('lambda_21AC')

    DispatchAsync2(0x00F7, 0x0001, lambda_21AC)

    @scena.Lambda('lambda_21BD')
    def lambda_21BD():
        ChrTurnDirection(0x00F8, 0x000B, 0)
        Yield()

        Jump('lambda_21BD')

    DispatchAsync2(0x00F8, 0x0001, lambda_21BD)

    @scena.Lambda('lambda_21CE')
    def lambda_21CE():
        ChrTurnDirection(0x00F9, 0x000B, 0)
        Yield()

        Jump('lambda_21CE')

    DispatchAsync2(0x00F9, 0x0001, lambda_21CE)

    OP_8E(0x000B, -2900, 0, 23000, 2000, 0x00)
    OP_8C(0x000B, 90, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    WaitForThreadExit(0x0025, 0x0001)
    WaitForThreadExit(0x0025, 0x0002)
    Fade(1000)
    SetChrChipByIndex(0x000B, 32)
    SetChrChipByIndex(0x0104, 15)
    SetChrChipByIndex(0x0101, 11)
    SetChrChipByIndex(0x0105, 17)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2236',
    )

    SetChrChipByIndex(0x00F7, 19)

    Jump('loc_223B')

    def _loc_2236(): pass

    label('loc_2236')

    SetChrChipByIndex(0x00F7, 13)

    def _loc_223B(): pass

    label('loc_223B')

    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0620450179V#700F#2P那么就开始吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450180V──准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_22B8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450181V#057F#1P嗯，随时可以开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E4')

    def _loc_22B8(): pass

    label('loc_22B8')

    ChrTalk(
        0x0103,
        (
            '#0030450182V#022F#1P嗯，随时可以开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22E4(): pass

    label('loc_22E4')

    ChrTalk(
        0x000B,
        (
            '#0620450183V#704F#2P好，那就接招吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Battle(0x00000C82, 0x00000000, 0x00, 0x0000, 0xFF)
    OP_28(0x006D, 0x01, 0x0004)
    OP_28(0x006D, 0x01, 0x0010)
    Call(1, 0x0003)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x232E
@scena.Code('func_03_232E')
def func_03_232E():
    EventBegin(0x00)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 19910, -29700, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2900, 0, 23000, 270)
    SetChrPos(0x00F7, 3900, 0, 24250, 270)
    SetChrPos(0x0104, 3900, 0, 21750, 270)
    SetChrPos(0x0105, 4900, 0, 23000, 270)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_23C1'),
        (0x00000001, 'loc_25DE'),
        (-1, 'loc_281E'),
    )

    def _loc_23C1(): pass

    label('loc_23C1')

    OP_28(0x006D, 0x01, 0x0020)
    SetChrChipByIndex(0x000B, 33)
    SetChrChipByIndex(0x0025, 24)
    SetChrChipByIndex(0x000F, 22)
    SetChrChipByIndex(0x0010, 22)
    SetChrSubChip(0x000B, 3)
    SetChrSubChip(0x0025, 3)
    SetChrSubChip(0x000F, 3)
    SetChrSubChip(0x0010, 3)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010450184V#1021F#3P总、总算是\n',
            '赢了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060450185V#042F#3P嗯、嗯……好不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_24AE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450186V#551F#2P呼，不好对付。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450187V想不到会被压制到如此程度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24FE')

    def _loc_24AE(): pass

    label('loc_24AE')

    ChrTalk(
        0x0103,
        (
            '#0030450188V#025F#2P啊，好危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450189V想不到会被压制到如此程度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24FE(): pass

    label('loc_24FE')

    ChrTalk(
        0x000B,
        (
            '#0620450190V#703F#1P了不起……我输得心服口服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_99(0x000B, 0x03, 0x00, 0x000007D0)
    Fade(1000)
    SetChrChipByIndex(0x000B, 3)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x00F7, 65535)
    SetChrChipByIndex(0x0105, 65535)
    SetChrChipByIndex(0x0104, 65535)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0620450191V#701F#1P连战之后还能\n',
            '做到这样，真是名不虚传。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450192V对士兵们来说\n',
            '你们为我们提供了最佳的榜样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x006D, 0x0002)
    OP_2C(0x006D, 0x05DC)

    Jump('loc_281E')

    def _loc_25DE(): pass

    label('loc_25DE')

    OP_28(0x006D, 0x01, 0x0040)
    SetChrChipByIndex(0x0104, 16)
    SetChrChipByIndex(0x0101, 12)
    SetChrChipByIndex(0x0105, 18)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2602',
    )

    SetChrChipByIndex(0x00F7, 20)

    Jump('loc_2607')

    def _loc_2602(): pass

    label('loc_2602')

    SetChrChipByIndex(0x00F7, 14)

    def _loc_2607(): pass

    label('loc_2607')

    SetChrSubChip(0x0104, 3)
    SetChrSubChip(0x0101, 3)
    SetChrSubChip(0x0105, 3)
    SetChrSubChip(0x00F7, 3)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010450193V#1021F#3P啊，好痛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450194V……输、输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060450195V#541F嗯，很遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_26E4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450196V#056F#2P可恶，真丢人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450187V想不到会被压制到如此程度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2734')

    def _loc_26E4(): pass

    label('loc_26E4')

    ChrTalk(
        0x0103,
        (
            '#0030450198V#025F#2P啊，失败了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450189V想不到会被压制到如此程度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2734(): pass

    label('loc_2734')

    ChrTalk(
        0x0104,
        (
            '#0040450200V#035F#3P呼，输得心服口服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrChipByIndex(0x000B, 3)
    SetChrChipByIndex(0x0025, 8)
    SetChrChipByIndex(0x0010, 5)
    SetChrChipByIndex(0x000F, 5)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0620450201V#701F#1P不，连战之后还能做到\n',
            '这种程度是很了不起的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450202V已经足够成为士兵们的\n',
            '好榜样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrChipByIndex(0x00F7, 65535)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0105, 65535)
    SetChrChipByIndex(0x0104, 65535)
    SetChrSubChip(0x00F7, 0)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0104, 0)
    SetChrSubChip(0x0105, 0)
    OP_0D()

    Jump('loc_281E')

    def _loc_281E(): pass

    label('loc_281E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2888',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450203V#053F#2P这是我们应该说的才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450204V虽然不甘心，可还是学到了不少东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28E8')

    def _loc_2888(): pass

    label('loc_2888')

    ChrTalk(
        0x0103,
        (
            '#0030450205V#020F#2P这是我们应该说的才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450206V虽然不甘心，可还是学到了不少东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28E8(): pass

    label('loc_28E8')

    ChrTalk(
        0x0101,
        (
            '#0010450207V#1015F#3P嗯，还是第一次被魔法\n',
            '折磨到这种程度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450208V#1006F让我也想重新\n',
            '检视一下自己的导力器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620450209V#701F#1P如果你们能这么想，\n',
            '那这场战斗就更有意义了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450210V问题并非是用什么，\n',
            '而在于怎样用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450211V无论是魔法还是战技，\n',
            '我觉得在这方面都是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450212V#031F原来如此，实在是真知灼见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620450213V#701F#1P我们王国军也要继续钻研，\n',
            '不甘落后于诸位游击士们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450214V为了王国的和平，今后也希望大家能和我们一起\n',
            '继续互相切磋下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450215V#1006F#3P嗯，我们也会努力进步的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450216V#1001F有机会的话\n',
            '再比试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2B71',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450217V#051F#2P是啊，请你们务必指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BA1')

    def _loc_2B71(): pass

    label('loc_2B71')

    ChrTalk(
        0x0103,
        (
            '#0030450218V#020F#2P是啊，请你们务必指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BA1(): pass

    label('loc_2BA1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_2BB1'),
        (0x00000001, 'loc_2C07'),
        (-1, 'loc_2C32'),
    )

    def _loc_2BB1(): pass

    label('loc_2BB1')

    ChrTalk(
        0x000B,
        (
            '#0620450219V#701F#1P嗯，一言为定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450220V老是输的话\n',
            '我晚上会睡不好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C32')

    def _loc_2C07(): pass

    label('loc_2C07')

    ChrTalk(
        0x000B,
        (
            '#0620450221V#701F#1P嗯，一言为定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C32')

    def _loc_2C32(): pass

    label('loc_2C32')

    OP_8C(0x000B, 45, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450222V#704F#1P──现在宣布训练结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450223V各位官兵辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【特别训练参加邀请】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2CE9',
    )

    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)

    Jump('loc_2CEE')

    def _loc_2CE9(): pass

    label('loc_2CE9')

    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)

    def _loc_2CEE(): pass

    label('loc_2CEE')

    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/C3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x2D05
@scena.Code('func_04_2D05')
def func_04_2D05():
    EventBegin(0x00)
    OP_6D(0, 0, 24840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6C(0, 0)
    OP_6B(2970, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2900, 0, 23000, 270)
    SetChrPos(0x00F7, 3900, 0, 24250, 270)
    SetChrPos(0x0104, 3900, 0, 21750, 270)
    SetChrPos(0x0105, 4900, 0, 23000, 270)
    SetChrChipByIndex(0x0104, 16)
    SetChrChipByIndex(0x0101, 12)
    SetChrChipByIndex(0x0105, 18)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2DA6',
    )

    SetChrChipByIndex(0x00F7, 20)

    Jump('loc_2DAB')

    def _loc_2DA6(): pass

    label('loc_2DA6')

    SetChrChipByIndex(0x00F7, 14)

    def _loc_2DAB(): pass

    label('loc_2DAB')

    SetChrSubChip(0x0104, 3)
    SetChrSubChip(0x0101, 3)
    SetChrSubChip(0x0105, 3)
    SetChrSubChip(0x00F7, 3)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0620450138V#704F#5P──到此为止！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010450225V#1021F#3P不、不好……\n',
            '输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2E67',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450226V#550F#1P切，大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E8D')

    def _loc_2E67(): pass

    label('loc_2E67')

    ChrTalk(
        0x0103,
        (
            '#0030450227V#025F#1P啊，大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E8D(): pass

    label('loc_2E8D')

    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450228V#702F呼，本来还希望\n',
            '你们再努力一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450229V#703F在战场上什么都有可能发生。\n',
            '这样的结果也是没办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450230V#704F──那么，我宣布训练结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450223V各位官兵辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_22(0x0106, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【特别训练参加邀请】',
            (TxtCtl.SetColor, 0x0),
            '失败了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x006D, 0x01, 0x0008)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2FD2',
    )

    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)

    Jump('loc_2FD7')

    def _loc_2FD2(): pass

    label('loc_2FD2')

    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)

    def _loc_2FD7(): pass

    label('loc_2FD7')

    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/C3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x2FEE
@scena.Code('func_05_2FEE')
def func_05_2FEE():
    OP_8C(0x000D, 135, 400)
    Sleep(800)

    OP_8C(0x000D, 90, 400)
    Sleep(800)

    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0x300E
@scena.Code('func_06_300E')
def func_06_300E():
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8C(0x000E, 180, 400)
    Sleep(800)

    OP_8C(0x000E, 90, 400)
    Sleep(800)

    OP_63(0x000E)
    OP_8C(0x000E, 135, 400)
    Sleep(800)

    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0007 offset: 0x304F
@scena.Code('func_07_304F')
def func_07_304F():
    OP_8C(0x000F, 0, 400)
    Sleep(800)

    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8C(0x000F, 90, 400)
    Sleep(800)

    OP_8C(0x000F, 45, 400)
    Sleep(800)

    OP_63(0x000F)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0008 offset: 0x3090
@scena.Code('func_08_3090')
def func_08_3090():
    OP_8C(0x0010, 90, 400)
    Sleep(800)

    OP_8C(0x0010, 45, 400)
    Sleep(800)

    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0009 offset: 0x30B0
@scena.Code('func_09_30B0')
def func_09_30B0():
    OP_94(0x01, 0x00FE, 0x0000, 0x00002710, 0x000007D0, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(1000)

    OP_A2(0x0002)
    OP_8C(0x00FE, 180, 400)
    OP_94(0x01, 0x00FE, 0x0000, 0x00000708, 0x000007D0, 0x00)
    OP_8C(0x00FE, 270, 400)
    OP_94(0x01, 0x00FE, 0x0000, 0x00000DAC, 0x000007D0, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x000A offset: 0x3102
@scena.Code('func_0A_3102')
def func_0A_3102():
    OP_94(0x01, 0x00FE, 0x0000, 0x00002710, 0x000007D0, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(1000)

    OP_A2(0x0003)
    OP_8C(0x00FE, 180, 400)
    OP_94(0x01, 0x00FE, 0x0000, 0x00000708, 0x000007D0, 0x00)
    OP_8C(0x00FE, 270, 400)
    OP_94(0x01, 0x00FE, 0x0000, 0x0000157C, 0x000007D0, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x000B offset: 0x3154
@scena.Code('func_0B_3154')
def func_0B_3154():
    OP_94(0x01, 0x00FE, 0x0000, 0x00002710, 0x000007D0, 0x00)
    SetChrSubChip(0x00FE, 0)
    OP_A6(0x0002)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x000C offset: 0x3173
@scena.Code('func_0C_3173')
def func_0C_3173():
    OP_94(0x01, 0x00FE, 0x0000, 0x00002710, 0x000007D0, 0x00)
    SetChrSubChip(0x00FE, 0)
    OP_A6(0x0003)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x000D offset: 0x3192
@scena.Code('func_0D_3192')
def func_0D_3192():
    OP_8E(0x000D, -3900, 0, 24250, 2000, 0x00)
    OP_8C(0x000D, 90, 400)

    Return()

# id: 0x000E offset: 0x31AE
@scena.Code('func_0E_31AE')
def func_0E_31AE():
    OP_8E(0x000E, -2900, 0, 23000, 2000, 0x00)
    OP_8C(0x000E, 90, 400)

    Return()

# id: 0x000F offset: 0x31CA
@scena.Code('func_0F_31CA')
def func_0F_31CA():
    OP_8E(0x000F, -4900, 0, 23000, 2000, 0x00)
    OP_8C(0x000F, 90, 400)

    Return()

# id: 0x0010 offset: 0x31E6
@scena.Code('func_10_31E6')
def func_10_31E6():
    OP_8E(0x0010, -3900, 0, 21750, 2000, 0x00)
    OP_8C(0x0010, 90, 400)

    Return()

# id: 0x0011 offset: 0x3202
@scena.Code('func_11_3202')
def func_11_3202():
    OP_99(0x00FE, 0x03, 0x00, 0x000007D0)
    OP_8C(0x00FE, 270, 0)
    SetChrChipByIndex(0x00FE, 10)
    OP_94(0x01, 0x00FE, 0x0000, 0x00001F40, 0x000007D0, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x322C
@scena.Code('func_12_322C')
def func_12_322C():
    SetChrChipByIndex(0x0104, 25)
    OP_99(0x0104, 0x00, 0x0E, 0x000007D0)
    WaitForThreadExit(0x0104, 0x0000)
    SetChrSubChip(0x0104, 14)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
