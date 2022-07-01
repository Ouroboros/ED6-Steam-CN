import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5311   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '歼灭天使玲'),
    TXT(0x02, '帕蒂尔·玛蒂尔'),
    TXT(0x03, '目标用照相机'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5311.x'
    header.mapIndex       = 1
    header.bgm            = 64
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x480E
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x108
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x108
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x108
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -32500,
            triggerZ            = 0,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = -32500,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x12C
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_146',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x76),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    Event(0, 0x000B)

    Jump('loc_174')

    def _loc_146(): pass

    label('loc_146')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_157',
    )

    OP_A3(0x10F1)
    Event(0, 0x000D)

    Jump('loc_174')

    def _loc_157(): pass

    label('loc_157')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_174',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 2, 0x223A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_174',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0003)

    def _loc_174(): pass

    label('loc_174')

    Return()

# id: 0x0001 offset: 0x175
@scena.Code('Init')
def Init():
    OP_22(0x01C3, 0x01, 0x64)
    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 3, 0x223B)),
            Expr.Return,
        ),
        'loc_18F',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0002, 0x0004)

    def _loc_18F(): pass

    label('loc_18F')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x463),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1AC(): pass

    label('loc_1AC')

    Call(0, 0x0002)
    OP_72(0x0000, 0x0004)

    def _loc_1B5(): pass

    label('loc_1B5')

    Return()

# id: 0x0002 offset: 0x1B6
@scena.Code('ReInit')
def ReInit():
    OP_D2(0x002701C7, 0x002701CC, 0x00)
    OP_D2(0x00270110, 0x00270120, 0x01)
    OP_D2(0x00270111, 0x00270121, 0x02)
    OP_D2(0x00270130, 0x00270140, 0x03)
    OP_D2(0x00270131, 0x00270141, 0x04)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_219'),
        (0x00000005, 'loc_230'),
        (0x00000003, 'loc_247'),
        (0x00000004, 'loc_25E'),
        (0x00000006, 'loc_275'),
        (0x00000007, 'loc_28C'),
        (0x00000008, 'loc_2A3'),
        (0x0000000A, 'loc_2BA'),
        (0x0000000E, 'loc_2D1'),
        (0x0000000F, 'loc_2E8'),
        (-1, 'loc_2FF'),
    )

    def _loc_219(): pass

    label('loc_219')

    OP_D2(0x000701D0, 0x000701DC, 0x05)
    OP_D2(0x000701D1, 0x000701DD, 0x06)

    Jump('loc_2FF')

    def _loc_230(): pass

    label('loc_230')

    OP_D2(0x00070218, 0x00070224, 0x05)
    OP_D2(0x00070219, 0x00070225, 0x06)

    Jump('loc_2FF')

    def _loc_247(): pass

    label('loc_247')

    OP_D2(0x000701E8, 0x000701F4, 0x05)
    OP_D2(0x000701E9, 0x000701F5, 0x06)

    Jump('loc_2FF')

    def _loc_25E(): pass

    label('loc_25E')

    OP_D2(0x0027036E, 0x0027037B, 0x05)
    OP_D2(0x0027036F, 0x0027037C, 0x06)

    Jump('loc_2FF')

    def _loc_275(): pass

    label('loc_275')

    OP_D2(0x00070230, 0x0007023C, 0x05)
    OP_D2(0x00070231, 0x0007023D, 0x06)

    Jump('loc_2FF')

    def _loc_28C(): pass

    label('loc_28C')

    OP_D2(0x00070248, 0x00070254, 0x05)
    OP_D2(0x00070249, 0x00070255, 0x06)

    Jump('loc_2FF')

    def _loc_2A3(): pass

    label('loc_2A3')

    OP_D2(0x00270176, 0x00270183, 0x05)
    OP_D2(0x00270177, 0x00270184, 0x06)

    Jump('loc_2FF')

    def _loc_2BA(): pass

    label('loc_2BA')

    OP_D2(0x000702B4, 0x000702BB, 0x05)
    OP_D2(0x000702B5, 0x000702BC, 0x06)

    Jump('loc_2FF')

    def _loc_2D1(): pass

    label('loc_2D1')

    OP_D2(0x002702D6, 0x002702E0, 0x05)
    OP_D2(0x002702D7, 0x002702E1, 0x06)

    Jump('loc_2FF')

    def _loc_2E8(): pass

    label('loc_2E8')

    OP_D2(0x002702C2, 0x002702CC, 0x05)
    OP_D2(0x002702C3, 0x002702CD, 0x06)

    Jump('loc_2FF')

    def _loc_2FF(): pass

    label('loc_2FF')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_330'),
        (0x00000005, 'loc_347'),
        (0x00000003, 'loc_35E'),
        (0x00000004, 'loc_375'),
        (0x00000006, 'loc_38C'),
        (0x00000007, 'loc_3A3'),
        (0x00000008, 'loc_3BA'),
        (0x0000000A, 'loc_3D1'),
        (0x0000000E, 'loc_3E8'),
        (0x0000000F, 'loc_3FF'),
        (-1, 'loc_416'),
    )

    def _loc_330(): pass

    label('loc_330')

    OP_D2(0x000701D0, 0x000701DC, 0x07)
    OP_D2(0x000701D1, 0x000701DD, 0x08)

    Jump('loc_416')

    def _loc_347(): pass

    label('loc_347')

    OP_D2(0x00070218, 0x00070224, 0x07)
    OP_D2(0x00070219, 0x00070225, 0x08)

    Jump('loc_416')

    def _loc_35E(): pass

    label('loc_35E')

    OP_D2(0x000701E8, 0x000701F4, 0x07)
    OP_D2(0x000701E9, 0x000701F5, 0x08)

    Jump('loc_416')

    def _loc_375(): pass

    label('loc_375')

    OP_D2(0x0027036E, 0x0027037B, 0x07)
    OP_D2(0x0027036F, 0x0027037C, 0x08)

    Jump('loc_416')

    def _loc_38C(): pass

    label('loc_38C')

    OP_D2(0x00070230, 0x0007023C, 0x07)
    OP_D2(0x00070231, 0x0007023D, 0x08)

    Jump('loc_416')

    def _loc_3A3(): pass

    label('loc_3A3')

    OP_D2(0x00070248, 0x00070254, 0x07)
    OP_D2(0x00070249, 0x00070255, 0x08)

    Jump('loc_416')

    def _loc_3BA(): pass

    label('loc_3BA')

    OP_D2(0x00270176, 0x00270183, 0x07)
    OP_D2(0x00270177, 0x00270184, 0x08)

    Jump('loc_416')

    def _loc_3D1(): pass

    label('loc_3D1')

    OP_D2(0x000702B4, 0x000702BB, 0x07)
    OP_D2(0x000702B5, 0x000702BC, 0x08)

    Jump('loc_416')

    def _loc_3E8(): pass

    label('loc_3E8')

    OP_D2(0x002702D6, 0x002702E0, 0x07)
    OP_D2(0x002702D7, 0x002702E1, 0x08)

    Jump('loc_416')

    def _loc_3FF(): pass

    label('loc_3FF')

    OP_D2(0x002702C2, 0x002702CC, 0x07)
    OP_D2(0x002702C3, 0x002702CD, 0x08)

    Jump('loc_416')

    def _loc_416(): pass

    label('loc_416')

    OP_D2(0x0027023E, 0x00270248, 0x09)
    OP_D2(0x00270244, 0x0027024E, 0x0A)
    OP_D2(0x002601CF, 0x002601D4, 0x0B)
    OP_D2(0x002601D0, 0x002601D5, 0x0C)
    OP_D2(0x00270246, 0x00270250, 0x0D)
    OP_D2(0x002600D3, 0x002600D8, 0x0E)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')

    Return()

# id: 0x0003 offset: 0x467
@scena.Code('func_03_467')
def func_03_467():
    Call(0, 0x0004)
    Call(0, 0x0005)

    Return()

# id: 0x0004 offset: 0x470
@scena.Code('func_04_470')
def func_04_470():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_491',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)

    def _loc_491(): pass

    label('loc_491')

    Call(0, 0x0002)
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    OP_A1(0x0009, 0x0000)
    SetChrPos(0x0009, -23640, 20000, 120, 90)
    OP_72(0x0000, 0x0004)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0001)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x34,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(18160, 0, 1020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 23580, 0, -420, 270)
    SetChrPos(0x0102, 23550, 0, 850, 270)
    SetChrPos(0x00F8, 24710, 0, -660, 270)
    SetChrPos(0x00F9, 24630, 0, 720, 270)

    @scena.Lambda('lambda_059E')
    def lambda_059E():
        OP_6B(3960, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_059E)

    @scena.Lambda('lambda_05AE')
    def lambda_05AE():
        OP_8E(0x00FE, 17750, 0, -420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05AE)

    Sleep(80)

    @scena.Lambda('lambda_05CE')
    def lambda_05CE():
        OP_8E(0x00FE, 17580, 0, 850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05CE)

    Sleep(100)

    @scena.Lambda('lambda_05EE')
    def lambda_05EE():
        OP_8E(0x00FE, 19050, 0, -660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_05EE)

    Sleep(150)

    @scena.Lambda('lambda_060E')
    def lambda_060E():
        OP_8E(0x00FE, 18880, 0, 720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_060E)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0008, 0)
    SetChrPos(0x0008, -18090, 0, 240, 90)
    ClearChrFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '少女的声音',
        (
            '#0220410593V嘻嘻……\n',
            '你们果然还是来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000001F4)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6ED',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_72B')

    def _loc_6ED(): pass

    label('loc_6ED')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_714',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_72B')

    def _loc_714(): pass

    label('loc_714')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_72B(): pass

    label('loc_72B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_757',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_795')

    def _loc_757(): pass

    label('loc_757')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_77E',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_795')

    def _loc_77E(): pass

    label('loc_77E')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_795(): pass

    label('loc_795')

    Sleep(500)

    OP_1D(0x6F)
    Sleep(500)

    @scena.Lambda('lambda_07A7')
    def lambda_07A7():
        OP_6D(-18810, 0, 1110, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_07A7)

    @scena.Lambda('lambda_07BF')
    def lambda_07BF():
        OP_67(0, 5310, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07BF)

    @scena.Lambda('lambda_07D7')
    def lambda_07D7():
        OP_6B(3430, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07D7)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_816',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410594V#065F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_816(): pass

    label('loc_816')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_85D',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410595V#178F<FIXME>《殲滅天使》……　　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A1')

    def _loc_85D(): pass

    label('loc_85D')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A1',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410596V#270F<FIXME>《殲滅天使》……　　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A1(): pass

    label('loc_8A1')

    ChrTalk(
        0x0101,
        (
            '#0010410597V#1002F……玲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410598V#1042F果然是你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08EB')
    def lambda_08EB():
        OP_8E(0x00FE, -8980, 0, -450, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08EB)

    @scena.Lambda('lambda_0906')
    def lambda_0906():
        OP_6D(-14650, 0, 2440, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0906)

    @scena.Lambda('lambda_091E')
    def lambda_091E():
        OP_67(0, 3910, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_091E)

    @scena.Lambda('lambda_0936')
    def lambda_0936():
        OP_6B(3680, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0936)

    @scena.Lambda('lambda_0946')
    def lambda_0946():
        OP_6E(311, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0946)

    Sleep(300)

    @scena.Lambda('lambda_095B')
    def lambda_095B():
        OP_8E(0x00FE, -8830, 0, 790, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_095B)

    Sleep(100)

    @scena.Lambda('lambda_097B')
    def lambda_097B():
        OP_8E(0x00FE, -7060, 0, -1100, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_097B)

    Sleep(300)

    OP_8E(0x00F9, -7100, 0, 370, 6000, 0x00)
    WaitForThreadExit(0x0102, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410599V#1306F#5P要打倒那三个人\n',
            '是很难的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410600V#261F但艾丝蒂尔和约修亚',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410601V是一定会来找玲的。\n',
            '玲一直都坚信不移呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410602V#1002F#6P玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410603V#1043F#6P如此说来……\n',
            '你还是准备同我们一战吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410604V#263F#5P嘿嘿嘿，该怎么办好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410605V以前都约定好了，\n',
            '再次见面时要把你们都杀死，\n',
            '但上次在城里相遇时又错过了好机会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410606V#1306F算啦，只要艾丝蒂尔的态度正确，\n',
            '玲饶了你们也是可以的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410607V#1015F#6P我的……态度？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410608V#261F#5P呵呵……很简单啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410609V#265F你只要收回上次\n',
            '对玲说过的话就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410610V#1020F#6P哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410611V#265F#5P上次你说过，玲待在\n',
            '『结社』是错误的，对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410612V只要你将这句话收回，\n',
            '玲就马上离开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410613V#261F怎么样，这交易不坏吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320674V#1026F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D2F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410615V#063F#4P小玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2F(): pass

    label('loc_D2F')

    ChrTalk(
        0x0102,
        (
            '#0020410616V#1042F#6P玲……\n',
            '这样的交易有什么价值呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410617V即使你听到了想听的话，\n',
            '但如果不是发自真心，也是没有意义的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410618V#1010F#6P约修亚……没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410619V#1025F接下来……\n',
            '就交给我可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410620V#1044F#2P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410621V#1035F明白了……拜托你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410622V#1025F#6P……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E88')
    def lambda_0E88():
        OP_6D(-16000, 0, 2180, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0E88)

    @scena.Lambda('lambda_0EA0')
    def lambda_0EA0():
        OP_67(0, 3400, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EA0)

    @scena.Lambda('lambda_0EB8')
    def lambda_0EB8():
        OP_6B(3440, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EB8)

    OP_8F(0x0101, -10450, 0, 30, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410623V#261F#5P呵呵，你终于肯\n',
            '答应了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410624V#265F好～快点说吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410625V说玲待在『结社』\n',
            '并没有任何错误。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410626V#1007F#6P玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410627V#1019F……撒娇也要\n',
            '有个限度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0220410628V#264F#5P…………咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410629V#1002F#6P世界不是以玲\n',
            '为中心运转的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410630V不会因为玲的任性\n',
            '要求而改变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410631V#1003F虽然玲拥有着\n',
            '如此强大的力量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410632V又有那位巨大的爸爸妈妈\n',
            '来帮助你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410633V#1010F但即便如此……\n',
            '也无法改变别人的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410634V#262F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410635V#1007F#6P不希望玲呆在结社，\n',
            '可能只是我一厢情愿的想法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410636V所以我并没打算勉强你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410637V#1025F但如果可能的话，\n',
            '我希望玲能明白一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410638V无论什么时候，你都可以\n',
            '像约修亚一样回头的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410639V#1040F#2P………艾丝蒂尔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410640V#1300F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410641V#266F…………是吗…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410642V好心好意给你们一个机会，\n',
            '你却枉费了我的苦心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410643V#1306F你真是个无可救药的大傻瓜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 13)
    SetChrSubChip(0x0008, 14)

    @scena.Lambda('lambda_1310')
    def lambda_1310():
        OP_99(0x0008, 0x0E, 0x08, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1310)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(200)

    @scena.Lambda('lambda_132A')
    def lambda_132A():
        OP_99(0x0008, 0x08, 0x02, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_132A)

    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_1344')
    def lambda_1344():
        OP_6B(3300, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1344)

    OP_22(0x01F9, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_1363')
    def lambda_1363():
        OP_99(0x0008, 0x02, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1363)

    SetChrChipByIndex(0x0008, 13)
    SetChrSubChip(0x0008, 0)
    OP_0D()

    @scena.Lambda('lambda_137E')
    def lambda_137E():
        OP_6D(-13120, 0, 1130, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_137E)

    @scena.Lambda('lambda_1396')
    def lambda_1396():
        OP_6B(3510, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1396)

    @scena.Lambda('lambda_13A6')
    def lambda_13A6():
        OP_6C(302000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_13A6)

    Sleep(500)

    SetChrChipByIndex(0x0008, 10)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_22(0x00D5, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_22(0x0113, 0x00, 0x50)

    @scena.Lambda('lambda_1424')
    def lambda_1424():
        OP_7C(0x0000000A, 0x0000000A, 0x000003E8, 0x000003E8)
        Yield()

        Jump('lambda_1424')

    DispatchAsync2(0x0101, 0x0002, lambda_1424)

    Sleep(500)

    CreateThread(0x0102, 0x00, 0x00, 0x0006)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0102, 0x0000)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 1)
    SetChrChipByIndex(0x0102, 3)
    SetChrChipByIndex(0x00F8, 5)
    SetChrChipByIndex(0x00F9, 7)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410644V#1003F#5P……各位，对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410645V这场战斗或许\n',
            '原本可以避免的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410646V#1035F#2P……你没有必要道歉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410647V#1040F你……已经把我想对那孩子\n',
            '说的话全部传达给她了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15DF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410648V#562F#4P我、我也\n',
            '觉得姐姐说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070410649V#062F玲一直这样下去的话…\n',
            '……我会好难过的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_15DF(): pass

    label('loc_15DF')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_163C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410650V#1061F#4P哈哈，指引迷途的羊羔\n',
            '回到正途，我也是双手赞成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_163C(): pass

    label('loc_163C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16A6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410651V#031F#4P呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040410652V小猫咪不乖的时候，\n',
            '偶尔也要好好调教一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_16A6(): pass

    label('loc_16A6')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16F4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410653V#051F#4P算啦，反正教育小鬼\n',
            '也是大人的职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_16F4(): pass

    label('loc_16F4')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1768',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410654V#277F<FIXME>……問題なかろう。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410655V子供を躾けるのも\n',
            '大人の義務だからな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_1768(): pass

    label('loc_1768')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17AE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410656V#070F#4P反正这也确实是\n',
            '大人的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_17AE(): pass

    label('loc_17AE')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17F5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410657V#1162F#4P我也……\n',
            '不会在这里退缩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_17F5(): pass

    label('loc_17F5')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1841',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410658V#027F#4P而且，这种事也算是\n',
            '大人的义务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C7')

    def _loc_1841(): pass

    label('loc_1841')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18C7',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410659V#176F<FIXME>……詳しい経緯は知らない。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410660V#170Fだが、私も正すべきところは\n',
            '正すべきだと思う。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18C7(): pass

    label('loc_18C7')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1907',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410661V#210F#4P哼哼……\n',
            '拿出气势来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1907(): pass

    label('loc_1907')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1956',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410662V#179F<FIXME>……私も全力を尽くさせてもらう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1956(): pass

    label('loc_1956')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_199E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410663V#027F#4P呵呵……\n',
            '大家都拿出气势来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_199E(): pass

    label('loc_199E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19DF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410664V#1162F#4P要拿出……\n',
            '气势来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_19DF(): pass

    label('loc_19DF')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A29',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410665V#074F#4P很好……\n',
            '各位，都拿出干劲来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1A29(): pass

    label('loc_1A29')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A89',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410666V#277F<FIXME>……この辺りでひとつ、\n',
            '気合を入れさせてもらうか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1A89(): pass

    label('loc_1A89')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AC9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410667V#051F#4P嘿……\n',
            '拿出气势来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1AC9(): pass

    label('loc_1AC9')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B17',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410668V#031F#4P呼呼……\n',
            '我会用满腔的爱来温暖玲的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1B17(): pass

    label('loc_1B17')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B5B',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410669V#1060F#4P嘿嘿……\n',
            '拿出气势来战斗吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B5B(): pass

    label('loc_1B5B')

    ChrTalk(
        0x0101,
        (
            '#0010320946V#1025F#5P大家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 201)
    OP_70(0x0000, 0x000000DC)
    Fade(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_71(0x0001, 0x0004)
    OP_6D(-14790, 8500, 0, 0)
    OP_67(0, -1000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(352, 0)
    SetChrPos(0x0008, -20420, 0, 80, 90)
    SetChrPos(0x0009, -23900, 20000, 120, 90)

    @scena.Lambda('lambda_1C17')
    def lambda_1C17():
        OP_7C(0x00000032, 0x00000032, 0x000003E8, 0x000003E8)
        Yield()

        Jump('lambda_1C17')

    DispatchAsync2(0x0101, 0x0002, lambda_1C17)

    OP_24(0x0113, 0x55)
    Sleep(100)

    OP_24(0x0113, 0x5A)
    Sleep(100)

    OP_24(0x0113, 0x5F)
    Sleep(100)

    OP_24(0x0113, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_1C56')
    def lambda_1C56():
        OP_8F(0x00FE, -23640, 0, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1C56)

    Sleep(500)

    @scena.Lambda('lambda_1C76')
    def lambda_1C76():
        OP_6D(-14790, 5500, 0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1C76)

    @scena.Lambda('lambda_1C8E')
    def lambda_1C8E():
        OP_67(0, 2200, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C8E)

    @scena.Lambda('lambda_1CA6')
    def lambda_1CA6():
        OP_6B(1600, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1CA6)

    WaitForThreadExit(0x0009, 0x0001)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 221)
    OP_70(0x0000, 0x000000F0)
    WaitForThreadExit(0x0009, 0x0001)
    OP_23(0x0113)
    OP_22(0x0088, 0x00, 0x64)
    OP_22(0x00F5, 0x00, 0x64)
    TerminateThread(0x0101, 0x02)
    OP_7C(0x00000000, 0x00000320, 0x00000BB8, 0x00000578)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 1)
    OP_70(0x0000, 0x00000028)
    Sleep(500)

    OP_22(0x03D4, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    Sleep(2000)

    @scena.Lambda('lambda_1D28')
    def lambda_1D28():
        OP_6D(-24500, 2400, 0, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1D28)

    @scena.Lambda('lambda_1D40')
    def lambda_1D40():
        OP_67(0, 1980, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D40)

    @scena.Lambda('lambda_1D58')
    def lambda_1D58():
        OP_6B(2460, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1D58)

    @scena.Lambda('lambda_1D68')
    def lambda_1D68():
        OP_6E(415, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1D68)

    Sleep(1000)

    OP_82(0x00, 0x02)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 9)
    OP_0D()
    WaitForThreadExit(0x0102, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410671V#1302F#5P……惹人生气……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410672V真是太惹人生气了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410673V#1304F『帕蒂尔·玛蒂尔』！\n',
            '解除限制吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410674V马力全开！\n',
            '歼灭艾丝蒂尔她们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Battle(0x00000463, 0x00000000, 0x00, 0x0000, 0xFF)

    Return()

# id: 0x0005 offset: 0x1E54
@scena.Code('func_05_1E54')
def func_05_1E54():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    Call(0, 0x0002)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    LoadEffect(0x02, 'map\\\\mp064_01.eff')
    LoadEffect(0x03, 'map\\\\mp065_01.eff')
    OP_A1(0x0009, 0x0000)
    SetChrPos(0x0009, -20000, 0, 5500, 135)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_B0(0x0000, 0x19)
    OP_6F(0x0000, 521)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0001)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x34,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0101, -9460, 0, -820, 270)
    SetChrPos(0x0102, -9160, 0, 360, 270)
    SetChrPos(0x00F8, -8020, 0, -1850, 270)
    SetChrPos(0x00F9, -7600, 0, -600, 270)
    SetChrChipByIndex(0x0101, 1)
    SetChrChipByIndex(0x0102, 3)
    SetChrChipByIndex(0x00F8, 5)
    SetChrChipByIndex(0x00F9, 7)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 0)
    SetChrPos(0x0008, -18600, 0, 2700, 0)
    OP_6D(-15000, 1300, 2300, 0)
    OP_67(0, 4100, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(326000, 0)
    OP_6E(394, 0)

    @scena.Lambda('lambda_1FE7')
    def lambda_1FE7():
        OP_6B(3000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1FE7)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0220410675V#1308F#6P为、为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410676V为什么『帕蒂尔·玛蒂尔』会输给\n',
            '艾丝蒂尔她们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020410677V#1035F#4P极限级战略人形兵器\n',
            '的控制系统好像还不稳定呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410678V#1043F大概是因为关节部分的负荷过重，\n',
            '导致无法运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0220410679V#1308F#5P……怎么会………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2158')
    def lambda_2158():
        OP_6D(-21870, 0, 8680, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2158)

    @scena.Lambda('lambda_2170')
    def lambda_2170():
        OP_67(0, 4720, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2170)

    OP_8C(0x0008, 0, 400)
    WaitForThreadExit(0x0101, 0x0000)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410680V#1303F#6P#3S『帕蒂尔·玛蒂尔』！！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410681V喂！站起来啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410682V快点把艾丝蒂尔她们\n',
            '全部杀光！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    Sleep(500)

    OP_22(0x03D4, 0x00, 0x64)
    Sleep(1000)

    Sleep(500)

    OP_22(0x00F4, 0x00, 0x64)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x23)
    OP_6F(0x0000, 481)
    OP_70(0x0000, 0x00000208)
    Sleep(5200)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    Sleep(200)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0220410683V#1307F#6P……啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 11)
    OP_22(0x00D1, 0x00, 0x50)
    OP_99(0x0008, 0x00, 0x04, 0x000004B0)
    Sleep(500)

    Fade(500)
    OP_6D(-15270, 0, 3370, 0)
    OP_67(0, 3950, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(326000, 0)
    OP_6E(394, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0220410684V#268F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410685V#1026F#6P玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2370')
    def lambda_2370():
        OP_6D(-18010, 0, 3600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2370)

    @scena.Lambda('lambda_2388')
    def lambda_2388():
        OP_67(0, 3800, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2388)

    @scena.Lambda('lambda_23A0')
    def lambda_23A0():
        OP_6B(3050, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_23A0)

    @scena.Lambda('lambda_23B0')
    def lambda_23B0():
        OP_8F(0x00FE, -15980, 0, 1970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_23B0)

    Sleep(800)

    @scena.Lambda('lambda_23D0')
    def lambda_23D0():
        OP_8F(0x00FE, -13910, 0, 1560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_23D0)

    Sleep(200)

    @scena.Lambda('lambda_23F0')
    def lambda_23F0():
        OP_8F(0x00FE, -13380, 0, -600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_23F0)

    Sleep(200)

    @scena.Lambda('lambda_2410')
    def lambda_2410():
        OP_8F(0x00FE, -12150, 0, 50, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2410)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410686V#268F#5P干什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410687V是艾丝蒂尔赢了！\n',
            '你们愿意怎样就请便……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410688V赶快去把终端解除，\n',
            '继续向上层前进吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410689V#1006F#6P……那虽然也很重要，\n',
            '但还是稍后再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410690V因为现在…你的事情最重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410691V#1303F#5P什么啊…艾丝蒂尔根本就不理解玲，\n',
            '玲的事情……你一点都不了解！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410692V既然这样，为什么……\n',
            '……为什么还要管我……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410693V#1012F#6P呵呵，那还用说吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410694V#1006F当然是因为我喜欢玲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410695V#1308F#5P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410696V#1002F#6P所以……有件事情，\n',
            '我必须要对玲做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410697V虽然很抱歉，不过我会下手轻一点的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410698V#1307F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_26E0')
    def lambda_26E0():
        OP_6D(-19570, 0, 4110, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_26E0)

    @scena.Lambda('lambda_26F8')
    def lambda_26F8():
        OP_6B(2630, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_26F8)

    OP_8F(0x0101, -17800, 0, 2450, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)

    @scena.Lambda('lambda_2726')
    def lambda_2726():
        OP_6B(2480, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2726)

    SetChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0002)
    SetChrFlags(0x0008, 0x0800)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 12)

    @scena.Lambda('lambda_2754')
    def lambda_2754():
        OP_99(0x00FE, 0x00, 0x0D, 0x000004B0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2754)

    Sleep(500)

    OP_20(0x00000000)
    OP_22(0x00A5, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0220410699V#1308F#5P…………啊…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410700V#40W……………被打了…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_1D(0x76)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410701V#1007F#6P做了坏事，\n',
            '当然要挨打啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410702V不然的话，你就永远体会不到\n',
            '他人的痛苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410703V#1006F我小的时候也是经常\n',
            '被爸爸用拳头揍的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410704V#1309F#5P#40W艾丝蒂尔……也是一样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410705V#40W明知道我很痛……\n',
            '但却还是不住手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410706V#40W和那些把玲……对玲做了很多坏事的人\n',
            '……完全一样吗………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410707V#1025F#6P是不是一样，\n',
            '玲可以自己来判断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410708V怎样……你真的这么认为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410709V#1309F#5P#40W…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410710V#40W………我……不知道…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410711V#1006F#6P那么……这样又如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A38')
    def lambda_2A38():
        OP_6D(-19900, 0, 4500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2A38)

    OP_99(0x0008, 0x0D, 0x13, 0x000005DC)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0220410712V#1307F#5P………啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410713V#1012F#6P什么都不用说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410714V……玲只要用自己心里\n',
            '的感觉来判断就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410715V#1307F#5P#40W……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410716V#40W……脑子里乱作一团，\n',
            '虽然搞不太清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x13, 0x15, 0x000003E8)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410717V#1309F#5P#40W不过被这样抱着…\n',
            '……感觉好像……也并不讨厌呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410718V#1016F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410719V#1309F#5P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410720V#268F………………我要回去了………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210711V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220410722V#1303F#5P#3S『帕蒂尔·玛蒂尔』！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410723V停止关节部位的制动器，\n',
            '启动辅助引擎的控制系统！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    Sleep(500)

    OP_22(0x03D4, 0x00, 0x64)
    Sleep(1500)

    @scena.Lambda('lambda_2D0F')
    def lambda_2D0F():
        OP_6D(-22500, 500, 9860, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2D0F)

    @scena.Lambda('lambda_2D27')
    def lambda_2D27():
        OP_67(0, 5300, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D27)

    @scena.Lambda('lambda_2D3F')
    def lambda_2D3F():
        OP_6B(3600, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D3F)

    Sleep(500)

    Play3DEffect(0x03, 0x00, 0x00, 'Frame86__jet_0', 0x00000000, 0xFFFFFE0C, 0x00000000, 0x003C, 0xFFA6, 0x00B4, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Play3DEffect(0x03, 0x01, 0x00, 'Frame87__jet_1', 0x00000000, 0xFFFFFE0C, 0x00000000, 0x001E, 0x0046, 0xFF4C, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)

    @scena.Lambda('lambda_2DBE')
    def lambda_2DBE():
        OP_8F(0x00FE, -20500, 1500, 6000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2DBE)

    OP_72(0x0000, 0x0020)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 521)
    OP_70(0x0000, 0x00000230)
    PlayEffect(0x01, 0x02, 0x0009, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00CC, 0x00, 0x64)
    OP_22(0x0113, 0x00, 0x64)
    OP_22(0x0114, 0x00, 0x64)
    Sleep(100)

    Fade(250)
    SetChrPos(0x0101, -18000, 0, 2450, 270)
    SetChrPos(0x0008, -18700, 0, 2660, 90)
    ClearChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0008, 0x0002)
    ClearChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0008, 0x0040)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 0)

    @scena.Lambda('lambda_2E83')
    def lambda_2E83():
        OP_8F(0x00FE, -19550, 0, 3040, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2E83)

    WaitForThreadExit(0x0008, 0x0000)
    OP_0D()
    Sleep(300)

    OP_8C(0x0101, 315, 400)

    @scena.Lambda('lambda_2EB0')
    def lambda_2EB0():
        OP_8F(0x00FE, -16460, 0, 1450, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2EB0)

    CreateThread(0x0102, 0x01, 0x00, 0x0008)
    Sleep(50)

    CreateThread(0x00F8, 0x01, 0x00, 0x0009)
    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, 0x000A)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0009, 0x0001)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_D8(0x00, 0x01F4)
    OP_B0(0x0000, 0x01)
    OP_6F(0x0000, 30)
    Sleep(300)

    Fade(500)
    OP_71(0x0001, 0x0004)
    OP_6D(-20000, 1800, 3140, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(291000, 0)
    OP_6E(598, 0)

    @scena.Lambda('lambda_2F57')
    def lambda_2F57():
        OP_8F(0x00FE, -20500, 0, 6000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2F57)

    WaitForThreadExit(0x0009, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x0000012C)
    OP_72(0x0000, 0x0020)
    OP_0D()
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 461)
    OP_70(0x0000, 0x000001E0)
    OP_22(0x0115, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_D8(0x00, 0x0320)
    OP_6F(0x0000, 381)
    OP_70(0x0000, 0x000001A4)
    Sleep(1000)

    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0008, 0x0004)
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_2FDB')
    def lambda_2FDB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2FDB')

    DispatchAsync2(0x0101, 0x0003, lambda_2FDB)

    @scena.Lambda('lambda_2FEC')
    def lambda_2FEC():
        OP_6D(-24790, 0, 4270, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2FEC)

    @scena.Lambda('lambda_3004')
    def lambda_3004():
        OP_67(0, 5140, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3004)

    @scena.Lambda('lambda_301C')
    def lambda_301C():
        OP_6B(2200, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_301C)

    OP_22(0x00A3, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 2)
    OP_96(0x0008, 0xFFFFAE3E, 0x00000E10, 0x000009C4, 0x00001194, 0x00000BB8)
    SetChrSubChip(0x0008, 7)
    ClearChrFlags(0x0008, 0x0001)
    OP_CF(0x0008, 0x00, 'Frame85__ren')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xA5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    OP_8C(0x0008, 315, 0)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410724V#1020F#5P玲……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0220410725V#1309F#5P我的脑子里很乱，\n',
            '所以想一个人好好想想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410726V艾丝蒂尔，你们就继续\n',
            '向塔顶前进吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410727V莱维在等着你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410728V#1002F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410729V#1040F#5P……是吗。\n',
            '谢谢你告诉我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410730V#1307F#5P没问题吗……约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410731V莱维看起来可是很认真的，\n',
            '似乎决心要阻止你们呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410732V#1035F#5P嗯……我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410733V#1040F但是，我也已经\n',
            '下了决心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410734V所以，不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410735V#1307F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410736V#268F那么，玲这就要走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_22(0x0114, 0x00, 0x64)
    OP_22(0x00CC, 0x00, 0x64)
    Play3DEffect(0x02, 0x00, 0x00, 'Frame86__jet_0', 0x00000000, 0xFFFFFD44, 0x00000000, 0x003C, 0xFFA6, 0x00B4, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Play3DEffect(0x02, 0x01, 0x00, 'Frame87__jet_1', 0x00000000, 0xFFFFFD44, 0x00000000, 0x001E, 0x0046, 0xFF4C, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)

    @scena.Lambda('lambda_3362')
    def lambda_3362():
        OP_8F(0x00FE, -20000, 2000, 5500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3362)

    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33BF',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_33FD')

    def _loc_33BF(): pass

    label('loc_33BF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33E6',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_33FD')

    def _loc_33E6(): pass

    label('loc_33E6')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_33FD(): pass

    label('loc_33FD')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3429',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3467')

    def _loc_3429(): pass

    label('loc_3429')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3450',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3467')

    def _loc_3450(): pass

    label('loc_3450')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_3467(): pass

    label('loc_3467')

    @scena.Lambda('lambda_346D')
    def lambda_346D():
        OP_6D(-20260, 4500, 4520, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_346D)

    @scena.Lambda('lambda_3485')
    def lambda_3485():
        OP_67(0, 3530, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3485)

    @scena.Lambda('lambda_349D')
    def lambda_349D():
        OP_6B(2820, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_349D)

    @scena.Lambda('lambda_34AD')
    def lambda_34AD():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_34AD)

    @scena.Lambda('lambda_34BD')
    def lambda_34BD():
        OP_6E(388, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_34BD)

    Sleep(800)

    OP_D8(0x00, 0x01F4)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x05)
    OP_6F(0x0000, 241)
    OP_70(0x0000, 0x00000104)

    @scena.Lambda('lambda_34ED')
    def lambda_34ED():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_34ED')

    DispatchAsync2(0x0101, 0x0003, lambda_34ED)

    @scena.Lambda('lambda_34FE')
    def lambda_34FE():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_34FE')

    DispatchAsync2(0x0102, 0x0003, lambda_34FE)

    @scena.Lambda('lambda_350F')
    def lambda_350F():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_350F')

    DispatchAsync2(0x00F8, 0x0003, lambda_350F)

    @scena.Lambda('lambda_3520')
    def lambda_3520():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3520')

    DispatchAsync2(0x00F9, 0x0003, lambda_3520)

    Sleep(300)

    @scena.Lambda('lambda_3536')
    def lambda_3536():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3536)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    PlayEffect(0x01, 0x02, 0x0009, 0, -1500, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrPos(0x0101, -13180, 0, -540, 270)
    SetChrPos(0x0102, -12060, 0, 230, 270)
    SetChrPos(0x00F8, -11210, 0, -1500, 270)
    SetChrPos(0x00F9, -11210, 0, -1500, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3697',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410737V#065F#5P小玲！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410738V#1020F#5P玲……等等！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410739V#1300F#5P……再见了。\n',
            '艾丝蒂尔，还有提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410740V虽然玲这就要走了……',
            TxtCtl.Enter,
            '\n',
            '#1301F不过我可不许你们死哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_372F')

    def _loc_3697(): pass

    label('loc_3697')

    ChrTalk(
        0x0101,
        (
            '#0010410738V#1020F#5P玲……等等！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220410742V#1300F#5P……再见了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220410743V虽然玲这就要走了……',
            TxtCtl.Enter,
            '\n',
            '#1301F不过我可不许你们死哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_372F(): pass

    label('loc_372F')

    @scena.Lambda('lambda_3735')
    def lambda_3735():
        OP_6D(-20220, 7330, 11320, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3735)

    @scena.Lambda('lambda_374D')
    def lambda_374D():
        OP_67(0, 2760, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_374D)

    @scena.Lambda('lambda_3765')
    def lambda_3765():
        OP_6B(4000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3765)

    @scena.Lambda('lambda_3775')
    def lambda_3775():
        OP_6C(327000, 4500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3775)

    @scena.Lambda('lambda_3785')
    def lambda_3785():
        OP_6E(362, 4500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3785)

    PlayEffect(0x02, 0x00, 0x0009, 4750, 2300, 0, 0, 0, 20, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x01, 0x0009, -4750, 2300, 0, 0, 0, 340, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_24(0x0113, 0x5F)

    @scena.Lambda('lambda_3803')
    def lambda_3803():
        OP_8C(0x00FE, 0, 50)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3803)

    @scena.Lambda('lambda_3811')
    def lambda_3811():
        OP_8F(0x00FE, -20000, 5000, 5500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3811)

    Sleep(100)

    @scena.Lambda('lambda_3831')
    def lambda_3831():
        OP_8F(0x00FE, -20000, 5000, 5500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3831)

    OP_82(0x02, 0x02)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0009, 0x0002)
    OP_72(0x0000, 0x0020)
    OP_D8(0x00, 0x01F4)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 261)
    OP_70(0x0000, 0x00000118)
    OP_22(0x0116, 0x00, 0x64)
    OP_73(0x0000)
    OP_D8(0x00, 0x01F4)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 281)
    OP_70(0x0000, 0x0000012C)
    PlayEffect(0x03, 0x02, 0x0009, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x03, 0x0009, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x0009, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x05, 0x0009, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x06, 0x0009, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x07, 0x0009, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0114, 0x00, 0x64)
    Sleep(1000)

    SetChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0001)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x34,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_82(0x00, 0x02)
    OP_82(0x01, 0x02)
    PlayEffect(0x02, 0x02, 0x0009, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x03, 0x0009, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x0009, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x05, 0x0009, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x06, 0x0009, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x07, 0x0009, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_3B5C')
    def lambda_3B5C():
        OP_6D(-21400, 6800, 20800, 1800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3B5C)

    @scena.Lambda('lambda_3B74')
    def lambda_3B74():
        OP_8F(0x00FE, -20000, 12000, 55500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B74)

    Sleep(300)

    @scena.Lambda('lambda_3B94')
    def lambda_3B94():
        OP_8F(0x00FE, -20000, 12000, 55500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B94)

    Sleep(200)

    @scena.Lambda('lambda_3BB4')
    def lambda_3BB4():
        OP_8F(0x00FE, -20000, 12000, 55500, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3BB4)

    Sleep(100)

    @scena.Lambda('lambda_3BD4')
    def lambda_3BD4():
        OP_8F(0x00FE, -20000, 12000, 55500, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3BD4)

    Sleep(100)

    @scena.Lambda('lambda_3BF4')
    def lambda_3BF4():
        OP_8F(0x00FE, -20000, 12000, 55500, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3BF4)

    Sleep(100)

    @scena.Lambda('lambda_3C14')
    def lambda_3C14():
        OP_8F(0x00FE, -20000, 12000, 55500, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3C14)

    Sleep(100)

    @scena.Lambda('lambda_3C34')
    def lambda_3C34():
        OP_8F(0x00FE, -20000, 12000, 55500, 32000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3C34)

    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    SetMapFlags(0x00100000)
    OP_A2(0x10FF)
    OP_A2(0x10FA)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x3C73
@scena.Code('func_06_3C73')
def func_06_3C73():
    @scena.Lambda('lambda_3C79')
    def lambda_3C79():
        OP_8F(0x00FE, -8080, 0, -320, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C79)

    Sleep(120)

    @scena.Lambda('lambda_3C99')
    def lambda_3C99():
        OP_8F(0x00FE, -6290, 0, 630, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3C99)

    Sleep(80)

    @scena.Lambda('lambda_3CB9')
    def lambda_3CB9():
        OP_8F(0x00FE, -6170, 0, -820, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3CB9)

    Sleep(100)

    @scena.Lambda('lambda_3CD9')
    def lambda_3CD9():
        OP_8F(0x00FE, -8090, 0, 950, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3CD9)

    WaitForThreadExit(0x0101, 0x0000)

    Return()

# id: 0x0007 offset: 0x3CF4
@scena.Code('func_07_3CF4')
def func_07_3CF4():
    @scena.Lambda('lambda_3CFA')
    def lambda_3CFA():
        OP_8E(0x00FE, 17550, 0, -220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3CFA)

    Sleep(40)

    @scena.Lambda('lambda_3D1A')
    def lambda_3D1A():
        OP_8E(0x00FE, 17580, 0, 850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3D1A)

    Sleep(100)

    @scena.Lambda('lambda_3D3A')
    def lambda_3D3A():
        OP_8E(0x00FE, 18910, 0, 1270, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3D3A)

    Sleep(50)

    OP_8E(0x00F9, 18830, 0, -780, 3000, 0x00)

    Return()

# id: 0x0008 offset: 0x3D69
@scena.Code('func_08_3D69')
def func_08_3D69():
    OP_8F(0x00FE, -15610, 0, 2110, 2000, 0x00)

    @scena.Lambda('lambda_3D83')
    def lambda_3D83():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3D83')

    DispatchAsync2(0x00FE, 0x0003, lambda_3D83)

    Return()

# id: 0x0009 offset: 0x3D8F
@scena.Code('func_09_3D8F')
def func_09_3D8F():
    OP_8F(0x00FE, -14700, 0, 0, 2000, 0x00)

    @scena.Lambda('lambda_3DA9')
    def lambda_3DA9():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3DA9')

    DispatchAsync2(0x00FE, 0x0003, lambda_3DA9)

    Return()

# id: 0x000A offset: 0x3DB5
@scena.Code('func_0A_3DB5')
def func_0A_3DB5():
    OP_8F(0x00FE, -13470, 0, 950, 2000, 0x00)

    @scena.Lambda('lambda_3DCF')
    def lambda_3DCF():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3DCF')

    DispatchAsync2(0x00FE, 0x0003, lambda_3DCF)

    Return()

# id: 0x000B offset: 0x3DDB
@scena.Code('func_0B_3DDB')
def func_0B_3DDB():
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
        'loc_3DF2',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)

    def _loc_3DF2(): pass

    label('loc_3DF2')

    OP_6D(-18300, 0, 10600, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -17750, 0, 10660, 0)
    SetChrPos(0x0102, -16059, 0, 9050, 0)
    SetChrPos(0x00F8, -17240, 0, 7850, 0)
    SetChrPos(0x00F9, -15710, 0, 7250, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410744V#1026F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410745V#1003F这样……没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410746V#1035F#6P嗯……放心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410747V#1040F毕竟发生了太多的事情，\n',
            '那孩子只是头脑比较混乱吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410748V虽然要花点时间……\n',
            '不过她终究会自己找到答案的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410236V#1025F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FF5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410750V#067F#6P嘿嘿……\n',
            '真希望以后能再见到她啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_3FF5(): pass

    label('loc_3FF5')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_403C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410751V#1168F#6P希望……\n',
            '今后能再遇到她啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_403C(): pass

    label('loc_403C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4080',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410752V#027F#6P呵呵……\n',
            '希望能再见到她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_4080(): pass

    label('loc_4080')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40C6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410753V#035F#6P呼……\n',
            '我很期待能再见到她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_40C6(): pass

    label('loc_40C6')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_410D',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410754V#1062F#6P嘿嘿……\n',
            '很期待能再见到她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_410D(): pass

    label('loc_410D')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4169',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410755V#051F#6P嘿嘿……走了啊，\n',
            '希望下次见面时，她能变得温顺点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_4169(): pass

    label('loc_4169')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41AD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410756V#070F#6P哈哈……\n',
            '期待能再见到她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_41AD(): pass

    label('loc_41AD')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4240',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410757V#179F<FIXME>……焦ることはない。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410758V#170F『人はいつでも後戻りが出来る』……\n',
            '君もそう言っていただろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CC')

    def _loc_4240(): pass

    label('loc_4240')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42CC',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410759V#210F<FIXME>へへ……\n',
            'まだ子供ってことだよね。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090410760Vそのうちにさ、機嫌直して\n',
            '帰ってくるんじゃないの？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42CC(): pass

    label('loc_42CC')

    ChrTalk(
        0x0101,
        (
            '#0010410761V#1025F#5P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410762V#1012F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 135, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010410763V#1006F#5P……那么……\n',
            '得转换一下心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410764V停止掉终端，然后继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410765V#1043F#6P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010410766V#1026F#5P啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410767V#1002F她说莱维\n',
            '在塔顶等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410768V#1043F#6P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020410769V#1035F#6P执行者Ｎｏ．Ⅱ。\n',
            '『剑帝』莱恩哈特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410770V战斗力在『执行者』之中\n',
            '也是数一数二的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410771V#1042F做好万全的准备向塔顶前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410772V#1002F#5P……明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4533',
    )

    OP_A2(0x2240)

    def _loc_4533(): pass

    label('loc_4533')

    OP_A2(0x223A)
    OP_28(0x009F, 0x01, 0x0400)
    OP_28(0x009F, 0x01, 0x0800)
    OP_20(0x000003E8)
    EventEnd(0x00)
    OP_1D(0x40)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x40),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000C offset: 0x4555
@scena.Code('func_0C_4555')
def func_0C_4555():
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '解除通向上层区域的隔离壁，\n',
            '以及传送门的锁定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5306._SN', 114, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x45BF
@scena.Code('func_0D_45BF')
def func_0D_45BF():
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
        'loc_45D6',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)

    def _loc_45D6(): pass

    label('loc_45D6')

    OP_6D(-33350, 0, 660, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3430, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -31400, 0, -720, 270)
    SetChrPos(0x0102, -31400, 0, 210, 270)
    SetChrPos(0x00F8, -29800, 0, -1260, 270)
    SetChrPos(0x00F9, -29800, 0, 10, 270)
    FadeIn(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '通往上层区域的隔离壁，\n',
            '以及传送门的锁定已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_71(0x0002, 0x0004)
    OP_0D()
    Sleep(500)

    OP_64(0x00, 0x0001)
    OP_A2(0x223B)
    OP_28(0x009F, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x46D4
@scena.Code('func_0E_46D4')
def func_0E_46D4():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_474E'),
        (0x00000001, 'loc_4754'),
        (-1, 'loc_475A'),
    )

    def _loc_474E(): pass

    label('loc_474E')

    OP_A2(0x1200)

    Jump('loc_475A')

    def _loc_4754(): pass

    label('loc_4754')

    OP_A2(0x1201)

    Jump('loc_475A')

    def _loc_475A(): pass

    label('loc_475A')

    Return()

# id: 0x000F offset: 0x475B
@scena.Code('func_0F_475B')
def func_0F_475B():
    FadeOut(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

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
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
