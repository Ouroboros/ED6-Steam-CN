import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3230_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3230   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '麻绪婆婆'),
    TXT(0x02, '内燃机'),
    TXT(0x03, '汽油罐'),
    TXT(0x04, '汽油罐'),
    TXT(0x05, '汽油罐'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3230.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x20A3
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
        ('ED6_DT07/CH02430._CH', 'ED6_DT07/CH02430P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458753,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966081,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966081,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966081,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x162
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x162
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x162
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 1, 0x2009)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_176',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0003)

    Jump('loc_1B9')

    def _loc_176(): pass

    label('loc_176')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 2, 0x200A)),
            Expr.Ez,
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_195',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0008)

    Jump('loc_1B9')

    def _loc_195(): pass

    label('loc_195')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 1, 0x2011)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B9',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000A)

    def _loc_1B9(): pass

    label('loc_1B9')

    Return()

# id: 0x0001 offset: 0x1BA
@scena.Code('Init')
def Init():
    OP_82(0x80, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1F3',
    )

    SetChrPos(0x0009, -20, 250, 8200, 270)
    OP_A1(0x0009, 0x0003)
    OP_72(0x0003, 0x0004)
    OP_22(0x00A1, 0x01, 0xC8)
    OP_22(0x00CF, 0x01, 0x64)
    CreateThread(0x0009, 0x01, 0x00, 0x0002)

    Jump('loc_207')

    def _loc_1F3(): pass

    label('loc_1F3')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_202',
    )

    Jump('loc_207')

    def _loc_202(): pass

    label('loc_202')

    OP_22(0x00A1, 0x01, 0xC8)

    def _loc_207(): pass

    label('loc_207')

    Return()

# id: 0x0002 offset: 0x208
@scena.Code('ReInit')
def ReInit():
    OP_22(0x00A1, 0x01, 0x64)
    OP_22(0x00CF, 0x01, 0x64)
    OP_C4(0x00, 0x00000020)
    def _loc_218(): pass

    label('loc_218')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_23A',
    )

    OP_7C(0x00000000, 0x00000014, 0x00000BB8, 0x00000064)
    Sleep(100)

    Jump('loc_218')

    def _loc_23A(): pass

    label('loc_23A')

    Return()

# id: 0x0003 offset: 0x23B
@scena.Code('func_03_23B')
def func_03_23B():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_252',
    )

    Call(0, 0x000B)
    Call(0, 0x000C)

    def _loc_252(): pass

    label('loc_252')

    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_6D(-1190, 0, 5790, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(284, 0)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    CreateThread(0x0102, 0x01, 0x00, 0x0005)
    CreateThread(0x00F8, 0x01, 0x00, 0x0006)
    CreateThread(0x00F9, 0x01, 0x00, 0x0007)

    @scena.Lambda('lambda_02CF')
    def lambda_02CF():
        OP_6D(-1190, 0, 5790, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_02CF)

    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010370316V#1015F#6P……果然是完全\n',
            '停止了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370317V#1035F#6P虽然是旧式的，\n',
            '不过这装置也是导力器驱动的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370318V#1043F不可能不受导力\n',
            '停止现象的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370319V#1007F#6P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370320V#1015F不过泵装置说到底\n',
            '就只是从那里的源泉把水\n',
            '传到澡堂吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370321V感觉应该还能有\n',
            '其他办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370322V#074F#6P不过要是用水桶运过去\n',
            '也不太现实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370323V#072F看来还是只能想办法\n',
            '让这个装置动起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BF')

    def _loc_4B2(): pass

    label('loc_4B2')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_53A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370324V#026F#6P不过要是用水桶运过去\n',
            '也不太现实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370325V#022F看来还是只能想办法\n',
            '让这个装置动起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BF')

    def _loc_53A(): pass

    label('loc_53A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370326V#053F#6P不过要是用水桶运过去\n',
            '也不太现实吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370327V#050F看来还是只能想办法\n',
            '让这个装置动起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BF(): pass

    label('loc_5BF')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_746',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370328V#1004F#4P说起来，『零力场发生器』\n',
            '就不能用在这个泵上吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020370329V#1035F#5P可能有点难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370330V#1040F博士说只能用在大小\n',
            '可以双手捧住的导力器上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370331V#1007F#4P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070370332V#064F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06FD')
    def lambda_06FD():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_06FD')

    DispatchAsync2(0x0102, 0x0001, lambda_06FD)

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020370333V#1044F#5P提妲，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0x00C2, 0x01, 0x0002)
    Call(0, 0x0009)

    Jump('loc_A4B')

    def _loc_746(): pass

    label('loc_746')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8CD',
    )

    OP_62(0x0106, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0106, 0x0102, 400)

    ChrTalk(
        0x0106,
        (
            '#0050370334V#052F#6P说起来，『零力场发生器』\n',
            '就不能用在这东西上吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07C1')
    def lambda_07C1():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07C1)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E7',
    )

    @scena.Lambda('lambda_07DC')
    def lambda_07DC():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_07DC)

    Jump('loc_7F5')

    def _loc_7E7(): pass

    label('loc_7E7')

    @scena.Lambda('lambda_07ED')
    def lambda_07ED():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_07ED)

    def _loc_7F5(): pass

    label('loc_7F5')

    ChrTurnDirection(0x0102, 0x0106, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020370335V#1035F#5P可能有点难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370336V#1040F博士说只能用在大小\n',
            '可以双手捧住的导力器上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050370337V#555F#6P唔……对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370338V#1007F#2P唔……\n',
            '就没什么好办法吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0x00C2, 0x01, 0x0002)
    EventEnd(0x00)

    Jump('loc_A4B')

    def _loc_8CD(): pass

    label('loc_8CD')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4B',
    )

    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030370339V#023F#6P说起来，『零力场发生器』\n',
            '对这个泵没用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0942')
    def lambda_0942():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0942)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_968',
    )

    @scena.Lambda('lambda_095D')
    def lambda_095D():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_095D)

    Jump('loc_976')

    def _loc_968(): pass

    label('loc_968')

    @scena.Lambda('lambda_096E')
    def lambda_096E():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_096E)

    def _loc_976(): pass

    label('loc_976')

    ChrTurnDirection(0x0102, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020370335V#1035F#5P可能有点难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370336V#1040F博士说只能用在大小\n',
            '可以双手捧住的导力器上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030370342V#025F#6P嗯……对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370338V#1007F#2P唔……\n',
            '就没什么好办法吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0x00C2, 0x01, 0x0002)
    EventEnd(0x00)

    def _loc_A4B(): pass

    label('loc_A4B')

    Return()

# id: 0x0004 offset: 0xA4C
@scena.Code('func_04_A4C')
def func_04_A4C():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 100, 0, -230, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0A73')
    def lambda_0A73():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0A73)

    OP_8E(0x00FE, 490, 0, 4590, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 315, 400)
    Sleep(500)

    OP_8C(0x00FE, 45, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0005 offset: 0xAB8
@scena.Code('func_05_AB8')
def func_05_AB8():
    Sleep(700)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 100, 0, -230, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0AE4')
    def lambda_0AE4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0AE4)

    OP_8E(0x00FE, -580, 0, 4510, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    Sleep(500)

    OP_8C(0x00FE, 45, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0006 offset: 0xB29
@scena.Code('func_06_B29')
def func_06_B29():
    Sleep(1400)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 100, 0, -230, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0B55')
    def lambda_0B55():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0B55)

    OP_8E(0x00FE, 850, 0, 3350, 2000, 0x00)

    Return()

# id: 0x0007 offset: 0xB76
@scena.Code('func_07_B76')
def func_07_B76():
    Sleep(2100)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 100, 0, -230, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0BA2')
    def lambda_0BA2():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0BA2)

    OP_8E(0x00FE, -650, 0, 3400, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0xBC3
@scena.Code('func_08_BC3')
def func_08_BC3():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_6D(-1190, 0, 5790, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(284, 0)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    CreateThread(0x0102, 0x01, 0x00, 0x0005)
    CreateThread(0x00F8, 0x01, 0x00, 0x0006)
    CreateThread(0x00F9, 0x01, 0x00, 0x0007)

    @scena.Lambda('lambda_0C42')
    def lambda_0C42():
        OP_6D(-1190, 0, 5790, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0C42)

    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010370344V#1015F#6P唔，要是能想办法让\n',
            '泵动就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370345V#1043F#6P嗯……要是『零力场发生器』\n',
            '能用就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070370332V#064F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D14')
    def lambda_0D14():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_0D14')

    DispatchAsync2(0x0102, 0x0001, lambda_0D14)

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020370333V#1044F#5P提妲，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0xD52
@scena.Code('func_09_D52')
def func_09_D52():
    @scena.Lambda('lambda_0D58')
    def lambda_0D58():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_0D58')

    DispatchAsync2(0x0101, 0x0001, lambda_0D58)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D84',
    )

    @scena.Lambda('lambda_0D76')
    def lambda_0D76():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_0D76')

    DispatchAsync2(0x00F9, 0x0001, lambda_0D76)

    Jump('loc_D95')

    def _loc_D84(): pass

    label('loc_D84')

    @scena.Lambda('lambda_0D8A')
    def lambda_0D8A():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_0D8A')

    DispatchAsync2(0x00F8, 0x0001, lambda_0D8A)

    def _loc_D95(): pass

    label('loc_D95')

    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070370348V#560F#6P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DC4')
    def lambda_0DC4():
        OP_6D(-270, 250, 7300, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DC4)

    @scena.Lambda('lambda_0DDC')
    def lambda_0DDC():
        OP_67(0, 6120, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DDC)

    @scena.Lambda('lambda_0DF4')
    def lambda_0DF4():
        OP_6B(2620, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0DF4)

    @scena.Lambda('lambda_0E04')
    def lambda_0E04():
        OP_6E(302, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0E04)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E59',
    )

    @scena.Lambda('lambda_0E21')
    def lambda_0E21():
        OP_8E(0x00FE, 1460, 0, 4650, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0E21)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_0E41')
    def lambda_0E41():
        OP_8E(0x00FE, -200, 250, 7570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0E41)

    Jump('loc_E94')

    def _loc_E59(): pass

    label('loc_E59')

    @scena.Lambda('lambda_0E5F')
    def lambda_0E5F():
        OP_8E(0x00FE, -1670, 0, 4630, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0E5F)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_0E7F')
    def lambda_0E7F():
        OP_8E(0x00FE, -200, 250, 7570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0E7F)

    def _loc_E94(): pass

    label('loc_E94')

    Sleep(500)

    WaitForThreadExit(0x0107, 0x0001)
    Sleep(700)

    OP_8C(0x0107, 315, 400)
    OP_8E(0x0107, -1350, 250, 7890, 3000, 0x00)
    OP_8C(0x0107, 270, 300)
    OP_62(0x0107, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1500)

    OP_8E(0x0107, -1380, 250, 6670, 3000, 0x00)
    OP_8C(0x0107, 270, 300)
    OP_62(0x0107, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1500)

    OP_8E(0x0107, 2500, 0, 5650, 4000, 0x00)
    OP_8C(0x0107, 90, 300)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1500)

    OP_8E(0x0107, 550, 250, 6470, 3000, 0x00)
    OP_8E(0x0107, 160, 250, 8840, 3000, 0x00)
    OP_8C(0x0107, 0, 400)
    OP_62(0x0107, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1500)

    ChrTalk(
        0x0107,
        (
            '#0070370349V#062F#6P那个，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370350V这边是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1084',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1043',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_1081')

    def _loc_1043(): pass

    label('loc_1043')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_106A',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_1081')

    def _loc_106A(): pass

    label('loc_106A')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_1081(): pass

    label('loc_1081')

    Jump('loc_10E9')

    def _loc_1084(): pass

    label('loc_1084')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10AB',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_10E9')

    def _loc_10AB(): pass

    label('loc_10AB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10D2',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_10E9')

    def _loc_10D2(): pass

    label('loc_10D2')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_10E9(): pass

    label('loc_10E9')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010370351V#1016F#6P我说……提妲？',
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
        'loc_1160',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370352V#555F#6P真没办法……\n',
            '又进入那种状态了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1160(): pass

    label('loc_1160')

    ChrTalk(
        0x0107,
        (
            '#0070370353V#560F#6P因为它不像近来的设备，\n',
            '没有设计那么复杂的\n',
            '导力结构……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370354V只要把这里和这里\n',
            '跟对面连接好的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370355V#064F啊，要做成等导力停止现象\n',
            '结束后马上就能复原的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370356V#062F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370357V#061F嗯……好像有办法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070370358V#560F#2P那个，\n',
            '说不定\n',
            '能让泵动起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_136C',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_132B',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1369')

    def _loc_132B(): pass

    label('loc_132B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1352',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1369')

    def _loc_1352(): pass

    label('loc_1352')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1369(): pass

    label('loc_1369')

    Jump('loc_13D1')

    def _loc_136C(): pass

    label('loc_136C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1393',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_13D1')

    def _loc_1393(): pass

    label('loc_1393')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13BA',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_13D1')

    def _loc_13BA(): pass

    label('loc_13BA')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_13D1(): pass

    label('loc_13D1')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010370359V#1004F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370360V#1044F#6P莫非……\n',
            '你要用『零力场发生器』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070370361V#067F#2P嘿嘿，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370362V#560F哥哥你也还记得吧？\n',
            '『内燃引擎』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370363V#1044F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370364V#1015F#6P内燃引擎……\n',
            '就是上次让工程机械动起来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070370365V#061F#2P嗯⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370366V#560F泵装置没有使用和\n',
            '工程机械一样复杂的结构……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370367V所以只要能让内燃引擎来驱动\n',
            '依靠导力器驱动的那部分的话，\n',
            '就能像原来一样工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370368V#1004F#6P原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370369V#1040F#6P这可真是个盲点呢。',
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
        'loc_1652',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370370V#051F#6P那么哪儿有那个\n',
            '内燃引擎呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16DB')

    def _loc_1652(): pass

    label('loc_1652')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1698',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370371V#020F#6P那么哪儿有那个\n',
            '放在哪里了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16DB')

    def _loc_1698(): pass

    label('loc_1698')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16DB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370372V#070F#6P那么哪儿有那个\n',
            '内燃引擎呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16DB(): pass

    label('loc_16DB')

    ChrTalk(
        0x0107,
        (
            '#0070370373V#560F#2P嗯，我听说飞船坪\n',
            '保管有内燃引擎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370374V#061F我想问问维修长\n',
            '先生就能知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370375V#1006F#6P飞船坪的格斯塔夫维修长是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370376V#1015F对了，要让内燃引擎活动\n',
            '是需要燃料的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020370377V#1040F#5P就是『汽油』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370378V说不定还是像上次一样去中央工房\n',
            '地下打听一下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-220, 0, 4610, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0000, -220, 0, 4610, 180)
    SetChrPos(0x0001, -220, 0, 4610, 180)
    SetChrPos(0x0002, -220, 0, 4610, 180)
    SetChrPos(0x0003, -220, 0, 4610, 180)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x200A)
    OP_28(0x00C2, 0x01, 0x0004)
    OP_28(0x00C2, 0x01, 0x0100)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x18E0
@scena.Code('func_0A_18E0')
def func_0A_18E0():
    EventBegin(0x00)
    SetChrPos(0x000A, -820, 0, 4090, 315)
    SetChrPos(0x000B, -40, 0, 4090, 315)
    SetChrPos(0x000C, 700, 0, 4090, 315)
    SetChrPos(0x0009, -30, 0, 5200, 90)
    OP_A1(0x000A, 0x0000)
    OP_72(0x0000, 0x0004)
    OP_A1(0x000B, 0x0001)
    OP_72(0x0001, 0x0004)
    OP_A1(0x000C, 0x0002)
    OP_72(0x0002, 0x0004)
    OP_A1(0x0009, 0x0003)
    OP_72(0x0003, 0x0004)
    SetChrPos(0x0101, 850, 0, 1380, 0)
    SetChrPos(0x0102, -350, 0, 1530, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19A2',
    )

    SetChrPos(0x00F8, 140, 0, 2750, 180)
    SetChrPos(0x00F9, 270, 0, 190, 0)

    Jump('loc_19C4')

    def _loc_19A2(): pass

    label('loc_19A2')

    SetChrPos(0x00F9, 140, 0, 2750, 180)
    SetChrPos(0x00F8, 270, 0, 190, 0)

    def _loc_19C4(): pass

    label('loc_19C4')

    OP_6D(-970, 0, 3460, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(319, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070370650V#560F#2P那么材料也齐全了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370651V#061F赶快开始改造\n',
            '泵装置吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370652V#1006F#6P啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370653V#1016F这倒是好，不过\n',
            '真的不需要帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370654V#560F#2P啊……\n',
            '那么那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370655V#061F你们能不能按改造\n',
            '图纸将零件分别放开？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370656V#1001F#6PＯＫ⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370657V#1040F#6P这点忙我们\n',
            '还是帮得了的。',
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
        'loc_1BB7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370658V#051F#6P那么就一起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C31')

    def _loc_1BB7(): pass

    label('loc_1BB7')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BF7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370659V#021F#6P那么让我也来\n',
            '帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C31')

    def _loc_1BF7(): pass

    label('loc_1BF7')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C31',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370660V#070F#6P嗯，让我也来帮忙吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C31(): pass

    label('loc_1C31')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(2000)

    OP_6D(-210, 250, 6480, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0009, -20, 250, 8200, 270)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    SetChrPos(0x0101, 450, 0, 4800, 0)
    SetChrPos(0x0102, -670, 0, 4590, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CE1',
    )

    SetChrPos(0x00F9, -60, 0, 3240, 0)

    Jump('loc_1CF2')

    def _loc_1CE1(): pass

    label('loc_1CE1')

    SetChrPos(0x00F8, -60, 0, 3240, 0)

    def _loc_1CF2(): pass

    label('loc_1CF2')

    SetChrPos(0x0107, -10, 250, 6830, 0)
    OP_D2(0x00070065, 0x0007006D, 0x03)
    SetChrSubChip(0x0107, 0)
    SetChrChipByIndex(0x0107, 3)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070370661V#062F#6P好……',
            TxtCtl.Enter,
            '\n',
            '#061F嗯，这样一来就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0107, 65535)
    OP_0D()
    OP_8C(0x0107, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370662V#1001F#6P太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370663V#1049F#6P辛苦了，提妲。',
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
        'loc_1E01',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370664V#051F#6P你还是那么\n',
            '手法娴熟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E8A')

    def _loc_1E01(): pass

    label('loc_1E01')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E47',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370665V#027F#6P还是和平时一样\n',
            '心灵手巧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E8A')

    def _loc_1E47(): pass

    label('loc_1E47')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E8A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370666V#070F#6P还是和平时一样\n',
            '干得漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E8A(): pass

    label('loc_1E8A')

    ChrTalk(
        0x0107,
        (
            '#0070370667V#067F#2P嘿嘿，还不知道\n',
            '能不能动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370668V赶快试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 0, 400)
    Sleep(300)

    Fade(500)
    SetChrChipByIndex(0x0107, 3)
    OP_0D()
    Sleep(300)

    OP_22(0x009C, 0x00, 0x64)
    Sleep(1000)

    OP_22(0x00A1, 0x01, 0xC8)
    OP_22(0x00CF, 0x01, 0x64)

    @scena.Lambda('lambda_1F11')
    def lambda_1F11():
        OP_7C(0x00000000, 0x00000032, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_1F11')

    DispatchAsync2(0x0101, 0x0002, lambda_1F11)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010340674V#1004F#6P哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370670V#1040F#6P泵的旋翼\n',
            '好像开始转动了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(ItemTable['汽油罐'], 3)
    RemoveItem(ItemTable['内燃引擎'], 1)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T3200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x1FA6
@scena.Code('func_0B_1FA6')
def func_0B_1FA6():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2023'),
        (0x00000001, 'loc_2029'),
        (-1, 'loc_202F'),
    )

    def _loc_2023(): pass

    label('loc_2023')

    OP_A2(0x1200)

    Jump('loc_202F')

    def _loc_2029(): pass

    label('loc_2029')

    OP_A2(0x1201)

    Jump('loc_202F')

    def _loc_202F(): pass

    label('loc_202F')

    Return()

# id: 0x000C offset: 0x2030
@scena.Code('func_0C_2030')
def func_0C_2030():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
