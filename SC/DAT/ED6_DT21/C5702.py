import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5702_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5702   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '强化猎兵'),
    TXT(0x02, '强化猎兵'),
    TXT(0x03, '强化猎兵'),
    TXT(0x04, '多伦'),
    TXT(0x05, '吉尔'),
    TXT(0x06, '空贼'),
    TXT(0x07, '空贼'),
    TXT(0x08, '空贼'),
    TXT(0x09, '空贼'),
    TXT(0x0A, '空贼'),
    TXT(0x0B, '空贼'),
    TXT(0x0C, '空贼'),
    TXT(0x0D, '空贼'),
    TXT(0x0E, '目标'),
    TXT(0x0F, '工业区域『法克特里亚』２'),
    TXT(0x10, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5702.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3F22
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
        ('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP'),
        ('ED6_DT07/CH00291._CH', 'ED6_DT07/CH00291P._CP'),
        ('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP'),
        ('ED6_DT07/CH00361._CH', 'ED6_DT07/CH00361P._CP'),
        ('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP'),
        ('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP'),
    ]

# id: 0x10002 offset: 0xDA
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 74170,
            z                   = 4000,
            y                   = -220080,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2BA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 66000,
            y           = 10000,
            z           = -124270,
            range       = 82300,
            dword_10    = 0x00004650,
            dword_14    = 0xFFFE1E7A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = 64500,
            y           = 10000,
            z           = -96700,
            range       = 83300,
            dword_10    = 0x00004650,
            dword_14    = 0xFFFE83EC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x2FA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2FA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_316',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0012)

    def _loc_316(): pass

    label('loc_316')

    Return()

# id: 0x0001 offset: 0x317
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFF2D10, 0xFFFC4EB0, 0x00230076)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x518),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_33E(): pass

    label('loc_33E')

    OP_22(0x01C7, 0x00, 0x64)
    OP_22(0x01C3, 0x01, 0x50)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x518),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_460',
    )

    OP_D2(0x0026020B, 0x00260210, 0x09)
    OP_D2(0x00270110, 0x00270120, 0x0A)
    OP_D2(0x00270111, 0x00270121, 0x0B)
    OP_D2(0x00270130, 0x00270140, 0x0C)
    OP_D2(0x00270131, 0x00270141, 0x0D)
    OP_D2(0x000702B4, 0x000702BB, 0x0E)
    OP_D2(0x000702B5, 0x000702BC, 0x0F)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_3BF'),
        (0x00000003, 'loc_3D6'),
        (0x00000004, 'loc_3ED'),
        (0x00000005, 'loc_404'),
        (0x00000006, 'loc_41B'),
        (0x00000007, 'loc_432'),
        (0x00000008, 'loc_449'),
        (-1, 'loc_460'),
    )

    def _loc_3BF(): pass

    label('loc_3BF')

    OP_D2(0x000701D0, 0x000701DC, 0x10)
    OP_D2(0x000701D1, 0x000701DD, 0x11)

    Jump('loc_460')

    def _loc_3D6(): pass

    label('loc_3D6')

    OP_D2(0x000701E8, 0x000701F4, 0x10)
    OP_D2(0x000701E9, 0x000701F5, 0x11)

    Jump('loc_460')

    def _loc_3ED(): pass

    label('loc_3ED')

    OP_D2(0x0027036E, 0x0027037B, 0x10)
    OP_D2(0x0027036F, 0x0027037C, 0x11)

    Jump('loc_460')

    def _loc_404(): pass

    label('loc_404')

    OP_D2(0x00070218, 0x00070224, 0x10)
    OP_D2(0x00070219, 0x00070225, 0x11)

    Jump('loc_460')

    def _loc_41B(): pass

    label('loc_41B')

    OP_D2(0x00070230, 0x0007023C, 0x10)
    OP_D2(0x00070231, 0x0007023D, 0x11)

    Jump('loc_460')

    def _loc_432(): pass

    label('loc_432')

    OP_D2(0x00070248, 0x00070254, 0x10)
    OP_D2(0x00070249, 0x00070255, 0x11)

    Jump('loc_460')

    def _loc_449(): pass

    label('loc_449')

    OP_D2(0x00270176, 0x00270183, 0x10)
    OP_D2(0x00270177, 0x00270184, 0x11)

    Jump('loc_460')

    def _loc_460(): pass

    label('loc_460')

    Return()

# id: 0x0002 offset: 0x461
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 0, 0x2220)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 1, 0x2221)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_46D',
    )

    Return()

    def _loc_46D(): pass

    label('loc_46D')

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
        'loc_492',
    )

    Call(0, 0x0015)
    Call(0, 0x0016)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_492(): pass

    label('loc_492')

    SetChrPos(0x0008, 37090, 16000, -74080, 135)
    SetChrPos(0x0009, 40420, 16000, -76420, 270)
    SetChrPos(0x000A, 37590, 16000, -77170, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x0008, 0x00, 0x06, 0x0002)
    CreateThread(0x0009, 0x00, 0x06, 0x0002)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)
    OP_E5(0x08, 0x00, 0x00)
    OP_E5(0x09, 0x00, 0x00)
    OP_E5(0x0A, 0x00, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51B',
    )

    OP_62(0x0107, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_558')

    def _loc_51B(): pass

    label('loc_51B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_541',
    )

    OP_62(0x0108, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_558')

    def _loc_541(): pass

    label('loc_541')

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_558(): pass

    label('loc_558')

    Sleep(1000)

    OP_12(0x000186A0, 0x0009C400, 0x00002710)

    @scena.Lambda('lambda_0570')
    def lambda_0570():
        OP_6D(62050, 16000, -34780, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0570)

    @scena.Lambda('lambda_0588')
    def lambda_0588():
        OP_67(0, 10390, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0588)

    @scena.Lambda('lambda_05A0')
    def lambda_05A0():
        OP_6B(14610, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05A0)

    @scena.Lambda('lambda_05B0')
    def lambda_05B0():
        OP_6C(343000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_05B0)

    @scena.Lambda('lambda_05C0')
    def lambda_05C0():
        OP_6E(599, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05C0)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    Fade(500)
    OP_11(0xAA, 0xC8, 0xFF, 0x000124F8, 0x0003A980, 0x00000000)
    OP_6D(37580, 16000, -75050, 0)
    OP_67(0, 4590, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(341, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_0D()
    Sleep(500)

    OP_E5(0x08, 0x00, 0x01)
    OP_E5(0x09, 0x00, 0x01)
    OP_E5(0x0A, 0x00, 0x01)

    ChrTalk(
        0x0009,
        (
            '#4220400041V#4P──想不到会被\n',
            '带来这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4220400042V#4P接下来要让我们\n',
            '干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210400043V#5P谁知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210400044V#5P不过教授和执行者们\n',
            '都出去了，看来应该不会\n',
            '留下什么重大的任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210400045V#5P顶多就是捕捉\n',
            '那帮空贼之类的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4230400046V#6P说到这个……\n',
            '利贝尔的飞船\n',
            '应该已经迫降了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4230400047V#6P准备好如何应对了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210400048V#5P命令上说，在教授他们\n',
            '回来之前暂时先放着不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210400049V#5P反正除了修理飞船之外，\n',
            '他们什么事情也不能做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_894',
    )

    SetChrPos(0x0101, 65519, 16000, -92680, 315)
    SetChrPos(0x0102, 65540, 16000, -94040, 315)
    SetChrPos(0x00F8, 67240, 16000, -92700, 315)
    SetChrPos(0x00F9, 67200, 16000, -94120, 315)

    Jump('loc_906')

    def _loc_894(): pass

    label('loc_894')

    SetChrPos(0x010B, 65519, 16000, -92680, 315)
    SetChrPos(0x0101, 65540, 16000, -94040, 315)
    SetChrPos(0x0102, 67240, 16000, -92700, 315)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E8',
    )

    SetChrPos(0x00F9, 67200, 16000, -94120, 315)

    Jump('loc_906')

    def _loc_8E8(): pass

    label('loc_8E8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_906',
    )

    SetChrPos(0x00F8, 67200, 16000, -94120, 315)

    def _loc_906(): pass

    label('loc_906')

    @scena.Lambda('lambda_090C')
    def lambda_090C():
        OP_6D(64690, 16000, -92130, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_090C)

    @scena.Lambda('lambda_0924')
    def lambda_0924():
        OP_67(0, 7850, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0924)

    OP_6C(294000, 5000)
    Fade(500)
    OP_6D(65129, 16000, -94170, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(243000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9D6',
    )

    SetChrPos(0x0101, 65519, 16000, -92680, 270)
    SetChrPos(0x0102, 65540, 16000, -94040, 0)
    SetChrPos(0x00F8, 67240, 16000, -92700, 270)
    SetChrPos(0x00F9, 67200, 16000, -94120, 0)

    Jump('loc_A48')

    def _loc_9D6(): pass

    label('loc_9D6')

    SetChrPos(0x010B, 65519, 16000, -92680, 270)
    SetChrPos(0x0101, 65540, 16000, -94040, 0)
    SetChrPos(0x0102, 67240, 16000, -92700, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A2A',
    )

    SetChrPos(0x00F9, 67200, 16000, -94120, 270)

    Jump('loc_A48')

    def _loc_A2A(): pass

    label('loc_A2A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A48',
    )

    SetChrPos(0x00F8, 67200, 16000, -94120, 0)

    def _loc_A48(): pass

    label('loc_A48')

    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1620',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400050V#1020F#6P（『古罗力亚斯』……\n',
            '  原来停在这里啊。）',
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
        'loc_AE6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400051V#065F#6P（哇……\n',
            '  好大的飞船……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_AE6(): pass

    label('loc_AE6')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400052V#1167F#6P（正如基库所说，\n',
            '  是在浮游都市的东侧呢……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060400053V#1162F（话说回来，还真是大啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_B6F(): pass

    label('loc_B6F')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BC8',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400054V#1063F#6P（嗯～近距离看起来\n',
            '  还真是大得不可思议……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_BC8(): pass

    label('loc_BC8')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C20',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400055V#025F#6P（嗯～近距离看起来\n',
            '  还真是大得不可思议……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_C20(): pass

    label('loc_C20')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C78',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400056V#032F#6P（嗯，就近看的话\n',
            '  还真是大得不可思议啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_C78(): pass

    label('loc_C78')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CCB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400057V#555F#6P（哟，近看的话\n',
            '  还真是大得不可思议呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCB(): pass

    label('loc_CCB')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D15',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400058V#072F#6P（不过……\n',
            '  看来是个好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E86')

    def _loc_D15(): pass

    label('loc_D15')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D5F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400059V#057F#6P（不过……\n',
            '  看来是个好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E86')

    def _loc_D5F(): pass

    label('loc_D5F')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DA9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400060V#030F#6P（不过……\n',
            '  看来是个好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E86')

    def _loc_DA9(): pass

    label('loc_DA9')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400061V#022F#6P（不过……\n',
            '  看来是个好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E86')

    def _loc_DF3(): pass

    label('loc_DF3')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3E',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400062V#1063F#6P（不过……\n',
            '  看来是个好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E86')

    def _loc_E3E(): pass

    label('loc_E3E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E86',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400063V#1162F#6P（不过……\n',
            '  看来是个好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E86(): pass

    label('loc_E86')

    ChrTalk(
        0x0102,
        (
            '#0020400064V#1035F#5P（教授不在，\n',
            '  确实是个绝佳的机会……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400065V#1042F（毕竟还要救出空贼团，\n',
            '  干脆一口气突入如何？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_0F18')
    def lambda_0F18():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0F18)

    Sleep(50)

    @scena.Lambda('lambda_0F2B')
    def lambda_0F2B():
        ChrTurnDirection(0x00F8, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0F2B)

    Sleep(250)

    ChrTalk(
        0x0101,
        (
            '#0010400066V#1004F#4P（等、等一下。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400067V#1015F（突入是无所谓，\n',
            '  不过是不是应该\n',
            '  给乔丝特打声招呼？？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400068V（因为要救出的是\n',
            '  她的哥哥们啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400069V#1044F#5P（艾丝蒂尔……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010400070V#1013F#4P（你、你可别误会哦，）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400071V（我可没替她在\n',
            '  着想什么的……\n',
            '  只是……出于游击士的道义而已。）',
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
        'loc_10EC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400072V#061F#6P（嘻嘻……\n',
            '  真像姐姐的风格。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125B')

    def _loc_10EC(): pass

    label('loc_10EC')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_113B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400073V#1168F#6P（呵呵……\n',
            '  真像艾丝蒂尔的风格。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125B')

    def _loc_113B(): pass

    label('loc_113B')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1182',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400074V#1061F#6P（哈哈……\n',
            '  不用害羞吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125B')

    def _loc_1182(): pass

    label('loc_1182')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11CC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400075V#031F#6P（呼……\n',
            '  没什么好害羞的吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125B')

    def _loc_11CC(): pass

    label('loc_11CC')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1212',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400076V#021F#6P（呵呵……\n',
            '  不用害羞吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125B')

    def _loc_1212(): pass

    label('loc_1212')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_125B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400077V#071F#6P（哈哈……\n',
            '  没什么好害羞的吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_125B(): pass

    label('loc_125B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12B1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400078V#051F#6P（那，这样的话\n',
            '  就暂时先返回埃尔赛尤吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_145C')

    def _loc_12B1(): pass

    label('loc_12B1')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1307',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400079V#070F#6P（好，这样的话\n',
            '  就暂时先返回埃尔赛尤吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_145C')

    def _loc_1307(): pass

    label('loc_1307')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_135F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400080V#035F#6P（呵呵，这样的话\n',
            '  就暂时先返回埃尔赛尤吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_145C')

    def _loc_135F(): pass

    label('loc_135F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13B5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400081V#027F#6P（嗯，这样的话\n',
            '  就暂时先返回埃尔赛尤吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_145C')

    def _loc_13B5(): pass

    label('loc_13B5')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_140C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400082V#1062F#6P（好，这样的话\n',
            '  就暂时先返回埃尔赛尤吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_145C')

    def _loc_140C(): pass

    label('loc_140C')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_145C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400083V#1168F#6P（这样的话\n',
            '  就暂时先返回埃尔赛尤吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_145C(): pass

    label('loc_145C')

    ChrTalk(
        0x0101,
        (
            '#0010400084V#1013F#4P（真、真是的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1529',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇看到过车站的终端】\n'),
            TXT(0x01, '【◇没看到过车站的终端】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_151D'),
        (0x00000001, 'loc_1523'),
        (-1, 'loc_1529'),
    )

    def _loc_151D(): pass

    label('loc_151D')

    OP_A2(0x222F)

    Jump('loc_1529')

    def _loc_1523(): pass

    label('loc_1523')

    OP_A3(0x222F)

    Jump('loc_1529')

    def _loc_1529(): pass

    label('loc_1529')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 7, 0x222F)),
            Expr.Return,
        ),
        'loc_1571',
    )

    ChrTalk(
        0x0102,
        (
            '#0020400085V#1040F#5P（那就快点使用\n',
            '  『光环轨道』吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15EB')

    def _loc_1571(): pass

    label('loc_1571')

    ChrTalk(
        0x0102,
        (
            '#0020400086V#1035F#5P（不过，要回埃尔赛尤的话，\n',
            '  先去找车站会比较快呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400087V#1040F（调查一下工业区域吧）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15EB(): pass

    label('loc_15EB')

    ChrTalk(
        0x0101,
        (
            '#0010400088V#1006F#4P（嗯，是啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2220)
    OP_28(0x009E, 0x01, 0x0004)

    Jump('loc_1D0E')

    def _loc_1620(): pass

    label('loc_1620')

    ChrTalk(
        0x0101,
        (
            '#0010400089V#1002F#5P（『古罗力亚斯』……\n',
            '  原来停在这里啊。）',
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
        'loc_16AA',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400090V#065F#6P（哇……\n',
            '  好大的飞船……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188F')

    def _loc_16AA(): pass

    label('loc_16AA')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1733',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400091V#1167F#6P（正如基库所说，\n',
            '  是在浮游都市的东侧呢……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060400053V#1162F（话说回来，还真是大啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188F')

    def _loc_1733(): pass

    label('loc_1733')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_178C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400093V#1063F#6P（嗯～近距离看起来\n',
            '  还真是大得不可思议……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188F')

    def _loc_178C(): pass

    label('loc_178C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17E4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400094V#025F#6P（嗯～近距离看起来\n',
            '  还真是大得不可思议……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188F')

    def _loc_17E4(): pass

    label('loc_17E4')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_183C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400095V#032F#6P（嗯，就近看的话\n',
            '  还真是大得不可思议啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188F')

    def _loc_183C(): pass

    label('loc_183C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_188F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400096V#555F#6P（哟，近看的话\n',
            '  还真是大得不可思议呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_188F(): pass

    label('loc_188F')

    OP_62(0x010B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x010B)
    Sleep(500)

    ChrTalk(
        0x010B,
        (
            '#0090400097V#212F#6P（总之……\n',
            '  敌人的头目不在，\n',
            '  看来是个好机会呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x010B, 90, 400)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400098V#210F#2P（谢谢你们了。\n',
            '  接下来我一个人去救哥哥们……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1957')
    def lambda_1957():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1957)

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_197B',
    )

    ChrTurnDirection(0x00F9, 0x010B, 400)

    Jump('loc_198F')

    def _loc_197B(): pass

    label('loc_197B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_198F',
    )

    ChrTurnDirection(0x00F8, 0x010B, 400)

    def _loc_198F(): pass

    label('loc_198F')

    ChrTalk(
        0x0101,
        (
            '#0010400099V#1019F#5P（我说你啊……\n',
            '  在说些什么梦话呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x010B, 0x0101, 400)

    ChrTalk(
        0x010B,
        (
            '#0090400100V#216F#4P（你、你说什么～！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400101V#1040F#6P（怎么可能让你\n',
            '  自己一个人进去呢？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400102V（我们也会帮忙的哦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400103V#215F#2P（可、可是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400104V#1022F#5P（哎～这也属于\n',
            '  游击士的工作范围嘛！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400105V#1009F（别说废话了，\n',
            '  快点确认一下装备吧！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400106V#413F#4P（……嗯、嗯…………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400107V#214F（我先声明，可别指望\n',
            '  我会感恩图报哦？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400108V（因为各种原因，\n',
            '  我不可想和你混熟！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400109V#1019F#5P（哼，这句话是我要说的吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400110V#1007F（真是的……\n',
            '  小小年纪一点也不可爱。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400111V#1052F#6P（咦……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400112V#1048F（总之做好准备后，\n',
            '  就将守卫打倒，入侵舰内吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x010B, 90, 400)

    ChrTalk(
        0x010B,
        (
            '#0090400113V#213F#2P（嗯、嗯。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400114V#1013F#5P（明～白。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2221)
    OP_28(0x009E, 0x01, 0x0008)
    def _loc_1D0E(): pass

    label('loc_1D0E')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(74210, 16000, -100620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 74210, 16000, -100620, 180)
    SetChrPos(0x0001, 74210, 16000, -100620, 180)
    SetChrPos(0x0002, 74210, 16000, -100620, 180)
    SetChrPos(0x0003, 74210, 16000, -100620, 180)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0003 offset: 0x1DB0
@scena.Code('func_03_1DB0')
def func_03_1DB0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_2698',
    )

    EventBegin(0x00)
    ChrTurnDirection(0x0102, 0x0000, 400)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_1DF8'),
        (0x00000001, 'loc_1E8B'),
        (0x0000000A, 'loc_1EF8'),
        (0x00000006, 'loc_1F8A'),
        (0x00000004, 'loc_201C'),
        (0x00000008, 'loc_20AF'),
        (0x00000002, 'loc_2144'),
        (0x00000003, 'loc_21DA'),
        (0x00000005, 'loc_226C'),
        (0x00000007, 'loc_2300'),
        (0x0000000E, 'loc_2394'),
        (0x0000000F, 'loc_24FF'),
        (-1, 'loc_2602'),
    )

    def _loc_1DF8(): pass

    label('loc_1DF8')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400116V再次潜入的话很危险。\n',
            '折回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270330V#1002F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_1E8B(): pass

    label('loc_1E8B')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400116V再次潜入的话很危险。\n',
            '折回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_1EF8(): pass

    label('loc_1EF8')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400116V再次潜入的话很危险。\n',
            '折回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400122V#212F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_1F8A(): pass

    label('loc_1F8A')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400116V再次潜入的话很危险。\n',
            '折回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070400125V#062F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_201C(): pass

    label('loc_201C')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400116V再次潜入的话很危险。\n',
            '折回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060400128V#1162F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_20AF(): pass

    label('loc_20AF')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400130V再次潜入的话很危险。\n',
            '折回去好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180400131V#1063F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_2144(): pass

    label('loc_2144')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400130V再次潜入的话很危险。\n',
            '折回去好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030270331V#022F嗯嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_21DA(): pass

    label('loc_21DA')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400130V再次潜入的话很危险。\n',
            '赶快回头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040400137V#032F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_226C(): pass

    label('loc_226C')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400130V再次潜入的话很危险。\n',
            '折回去好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050270332V#050F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_2300(): pass

    label('loc_2300')

    ChrTalk(
        0x0102,
        (
            '#0020400115V#1042F现在前面的警戒应该\n',
            '变得相当森严了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400130V再次潜入的话很危险。\n',
            '折回去好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080400143V#072F好！　明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_2394(): pass

    label('loc_2394')

    ChrTalk(
        0x0102,
        (
            '#0020400144V#1042F<FIXME>僕たちが一度潜入したことで、\n',
            'この先の警戒は相当\n',
            '厳しくなっているはずです。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400145V特に用もありませんし、\n',
            'ここは引き返しましょう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100400146V#176F<FIXME>……確かにそうだな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100400147V#178F王都を襲撃した連中……\n',
            '余裕があれば全員捕縛して\n',
            'やりたいところだが……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100400148V今は《中枢塔》の探索に\n',
            '専念するとしよう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_24FF(): pass

    label('loc_24FF')

    ChrTalk(
        0x0110,
        (
            '#0110400149V#270F<FIXME>《結社》の船か……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400144V#1042F<FIXME>僕たちが一度潜入したことで、\n',
            'この先の警戒は相当\n',
            '厳しくなっているはずです。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400145V特に用もありませんし、\n',
            'ここは引き返しましょう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0110400152V#272F<FIXME>……心得た。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2602')

    def _loc_2602(): pass

    label('loc_2602')

    Sleep(100)

    Fade(500)
    OP_6D(74210, 16000, -100620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 74210, 16000, -100620, 180)
    SetChrPos(0x0001, 74210, 16000, -100620, 180)
    SetChrPos(0x0002, 74210, 16000, -100620, 180)
    SetChrPos(0x0003, 74210, 16000, -100620, 180)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_2D74')

    def _loc_2698(): pass

    label('loc_2698')

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
        'loc_26BD',
    )

    Call(0, 0x0015)
    Call(0, 0x0016)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_26BD(): pass

    label('loc_26BD')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AB8',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_26F7'),
        (0x00000001, 'loc_2772'),
        (0x00000006, 'loc_27D4'),
        (0x00000004, 'loc_2839'),
        (0x00000008, 'loc_2897'),
        (0x00000002, 'loc_2903'),
        (0x00000003, 'loc_2969'),
        (0x00000005, 'loc_29DD'),
        (0x00000007, 'loc_2A49'),
        (-1, 'loc_2AB5'),
    )

    def _loc_26F7(): pass

    label('loc_26F7')

    ChrTalk(
        0x0101,
        (
            '#0010400153V#1007F（……必须先返回埃尔赛尤\n',
            '  去叫乔丝特才行。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400154V#1019F（真是的……\n',
            '  让人这么费事。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_2772(): pass

    label('loc_2772')

    ChrTalk(
        0x0102,
        (
            '#0020400155V#1044F（不行……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400156V#1042F（先返回埃尔赛尤\n',
            '  去叫乔丝特过来吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_27D4(): pass

    label('loc_27D4')

    ChrTalk(
        0x0107,
        (
            '#0070400157V#065F（不、不行。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400158V（首先要返回埃尔赛尤\n',
            '  去叫空贼姐姐来才行……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_2839(): pass

    label('loc_2839')

    ChrTalk(
        0x0105,
        (
            '#0060400159V#1162F（不行……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060400160V（得先返回埃尔赛尤\n',
            '  把乔丝特叫来才行。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_2897(): pass

    label('loc_2897')

    ChrTalk(
        0x0109,
        (
            '#0180400161V#1064F（且慢……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180400162V#1060F（必须先返回埃尔赛尤\n',
            '  把空贼小姑娘带来才行呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_2903(): pass

    label('loc_2903')

    ChrTalk(
        0x0103,
        (
            '#0030400163V#023F（等等……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400164V#020F（先得返回埃尔赛尤\n',
            '  把那小姑娘带来才行呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_2969(): pass

    label('loc_2969')

    ChrTalk(
        0x0104,
        (
            '#0040400165V#035F（呵呵，这可不行。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400166V#037F（首先得返回埃尔赛尤\n',
            '  把那只小猫咪给带来才行呢㈱）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_29DD(): pass

    label('loc_29DD')

    ChrTalk(
        0x0106,
        (
            '#0050400167V#052F（等等……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400168V#053F（先得返回埃尔赛尤\n',
            '  把那个空贼小姑娘带来才行呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_2A49(): pass

    label('loc_2A49')

    ChrTalk(
        0x0108,
        (
            '#0080400169V#073F（等等……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400170V#070F（先得返回埃尔赛尤\n',
            '  把那个空贼小姑娘带来才行呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB5')

    def _loc_2AB5(): pass

    label('loc_2AB5')

    Jump('loc_2CE1')

    def _loc_2AB8(): pass

    label('loc_2AB8')

    OP_A2(0x22D4)
    Fade(500)
    OP_6D(74330, 16000, -99550, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0102, 74210, 16000, -98340, 180)
    SetChrPos(0x0101, 74330, 16000, -100940, 0)
    SetChrPos(0x00F8, 72760, 16000, -100170, 45)
    SetChrPos(0x00F9, 75790, 16000, -100350, 315)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020400171V#1042F（一旦进入了舰内，\n',
            '  在救出吉尔他们之前\n',
            '  就没有多余时间逃出来了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400172V（要突入『古罗力亚斯』吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

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
            TXT(0x00, '【突入】\n'),
            TXT(0x01, '【还要准备】\n'),
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
    FadeIn(100, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C29',
    )

    Jump('loc_2CE1')

    def _loc_2C29(): pass

    label('loc_2C29')

    ChrTalk(
        0x0101,
        (
            '#0010400173V#1002F#6P（ＯＫ！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010B, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010400174V#1006F#6P（乔丝特……\n',
            '好好跟着我们哦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400175V#214F#5P（这才是我要对你说的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0004)

    def _loc_2CE1(): pass

    label('loc_2CE1')

    Sleep(100)

    Fade(500)
    OP_6D(74210, 16000, -100620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 74210, 16000, -100620, 180)
    SetChrPos(0x0001, 74210, 16000, -100620, 180)
    SetChrPos(0x0002, 74210, 16000, -100620, 180)
    SetChrPos(0x0003, 74210, 16000, -100620, 180)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x02)
    def _loc_2D74(): pass

    label('loc_2D74')

    Return()

# id: 0x0004 offset: 0x2D75
@scena.Code('func_04_2D75')
def func_04_2D75():
    Call(0, 0x0005)
    Call(0, 0x0006)

    Return()

# id: 0x0005 offset: 0x2D7E
@scena.Code('func_05_2D7E')
def func_05_2D7E():
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DA3',
    )

    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationAddMember(ChrTable['乔丝特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF9, 0xFF)

    def _loc_2DA3(): pass

    label('loc_2DA3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DBE',
    )

    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationAddMember(ChrTable['乔丝特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)

    def _loc_2DBE(): pass

    label('loc_2DBE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DD9',
    )

    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationAddMember(ChrTable['乔丝特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)

    def _loc_2DD9(): pass

    label('loc_2DD9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DF4',
    )

    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationAddMember(ChrTable['乔丝特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xF9, 0xFF)

    def _loc_2DF4(): pass

    label('loc_2DF4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E0F',
    )

    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationAddMember(ChrTable['乔丝特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF9, 0xFF)

    def _loc_2E0F(): pass

    label('loc_2E0F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E2A',
    )

    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationAddMember(ChrTable['乔丝特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['金'], 0xF9, 0xFF)

    def _loc_2E2A(): pass

    label('loc_2E2A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E45',
    )

    FormationDelMember(0x08, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationAddMember(ChrTable['乔丝特'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['凯文神父'], 0xF9, 0xFF)

    def _loc_2E45(): pass

    label('loc_2E45')

    OP_D2(0x00270312, 0x0027031C, 0x06)
    OP_D2(0x00270316, 0x00270320, 0x08)
    OP_D2(0x00270110, 0x00270120, 0x0A)
    OP_D2(0x00270111, 0x00270121, 0x0B)
    OP_D2(0x00270130, 0x00270140, 0x0C)
    OP_D2(0x00270131, 0x00270141, 0x0D)
    OP_D2(0x000702B4, 0x000702BB, 0x0E)
    OP_D2(0x000702B5, 0x000702BC, 0x0F)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2EBA'),
        (0x00000003, 'loc_2ED1'),
        (0x00000004, 'loc_2EE8'),
        (0x00000005, 'loc_2EFF'),
        (0x00000006, 'loc_2F16'),
        (0x00000007, 'loc_2F2D'),
        (0x00000008, 'loc_2F44'),
        (-1, 'loc_2F5B'),
    )

    def _loc_2EBA(): pass

    label('loc_2EBA')

    OP_D2(0x000701D0, 0x000701DC, 0x10)
    OP_D2(0x000701D1, 0x000701DD, 0x11)

    Jump('loc_2F5B')

    def _loc_2ED1(): pass

    label('loc_2ED1')

    OP_D2(0x000701E8, 0x000701F4, 0x10)
    OP_D2(0x000701E9, 0x000701F5, 0x11)

    Jump('loc_2F5B')

    def _loc_2EE8(): pass

    label('loc_2EE8')

    OP_D2(0x0027036E, 0x0027037B, 0x10)
    OP_D2(0x0027036F, 0x0027037C, 0x11)

    Jump('loc_2F5B')

    def _loc_2EFF(): pass

    label('loc_2EFF')

    OP_D2(0x00070218, 0x00070224, 0x10)
    OP_D2(0x00070219, 0x00070225, 0x11)

    Jump('loc_2F5B')

    def _loc_2F16(): pass

    label('loc_2F16')

    OP_D2(0x00070230, 0x0007023C, 0x10)
    OP_D2(0x00070231, 0x0007023D, 0x11)

    Jump('loc_2F5B')

    def _loc_2F2D(): pass

    label('loc_2F2D')

    OP_D2(0x00070248, 0x00070254, 0x10)
    OP_D2(0x00070249, 0x00070255, 0x11)

    Jump('loc_2F5B')

    def _loc_2F44(): pass

    label('loc_2F44')

    OP_D2(0x00270176, 0x00270183, 0x10)
    OP_D2(0x00270177, 0x00270184, 0x11)

    Jump('loc_2F5B')

    def _loc_2F5B(): pass

    label('loc_2F5B')

    OP_D2(0x00270313, 0x0027031D, 0x12)
    OP_D2(0x00270326, 0x00270330, 0x13)
    OP_D2(0x00270327, 0x00270331, 0x14)
    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x010B, 14)
    SetChrChipByIndex(0x00F9, 16)
    OP_6D(37580, 16000, -75050, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 37090, 16000, -74080, 135)
    SetChrPos(0x0009, 40420, 16000, -76420, 270)
    SetChrPos(0x000A, 37590, 16000, -77170, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    SetChrPos(0x0101, 52000, 16000, -80320, 270)
    SetChrPos(0x0102, 53880, 16000, -80190, 270)
    SetChrPos(0x010B, 54210, 16000, -82160, 270)
    SetChrPos(0x00F9, 56010, 16000, -82070, 270)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    SetChrPos(0x0015, 40620, 16000, -75270, 0)
    OP_20(0x000003E8)
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 41530, 16000, -75450, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 40550, 16000, -79030, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(150)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    SetChrChipByIndex(0x0009, 7)

    @scena.Lambda('lambda_316E')
    def lambda_316E():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_316E)

    OP_96(0x0009, 0x0000986C, 0x00003E80, 0xFFFED702, 0x00000064, 0x00001B58)
    SetChrChipByIndex(0x0009, 8)
    SetChrSubChip(0x0009, 3)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_31E1')
    def lambda_31E1():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_31E1)

    Sleep(100)

    OP_8C(0x000A, 90, 400)
    CreateThread(0x0008, 0x01, 0x00, 0x0007)
    Sleep(100)

    CreateThread(0x000A, 0x01, 0x00, 0x0008)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#4210400176V#5P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4230400177V#5P敌、敌袭！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_1D(0x2C)
    Sleep(500)

    @scena.Lambda('lambda_3261')
    def lambda_3261():
        OP_6D(41870, 16000, -75460, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3261)

    @scena.Lambda('lambda_3279')
    def lambda_3279():
        OP_67(0, 3690, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3279)

    @scena.Lambda('lambda_3291')
    def lambda_3291():
        OP_6B(3300, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3291)

    @scena.Lambda('lambda_32A1')
    def lambda_32A1():
        OP_6C(315000, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_32A1)

    @scena.Lambda('lambda_32B1')
    def lambda_32B1():
        OP_6E(322, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_32B1)

    CreateThread(0x0101, 0x00, 0x00, 0x000A)
    CreateThread(0x0102, 0x00, 0x00, 0x000B)
    CreateThread(0x00F9, 0x00, 0x00, 0x000D)
    CreateThread(0x010B, 0x00, 0x00, 0x000C)
    CreateThread(0x0009, 0x01, 0x00, 0x0009)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x010B, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#4220400178V#5P你们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4230400179V#5P你、你们的飞船\n',
            '应该还在修理中吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4230400180V你们是怎么来到这里的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400181V#1006F#6P不好意思，我们是\n',
            '用自己的双脚一路走到这里的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400182V#214F#6P把哥哥他们交出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_33F8')
    def lambda_33F8():
        OP_6D(42000, 16000, -76180, 350)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33F8)

    @scena.Lambda('lambda_3410')
    def lambda_3410():
        OP_67(0, 4860, -10000, 350)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3410)

    @scena.Lambda('lambda_3428')
    def lambda_3428():
        OP_6B(2650, 350)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3428)

    @scena.Lambda('lambda_3438')
    def lambda_3438():
        OP_8F(0x00FE, 43650, 16000, -77880, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3438)

    Sleep(20)

    @scena.Lambda('lambda_3458')
    def lambda_3458():
        OP_8F(0x00FE, 43730, 16000, -76620, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_3458)

    SetChrChipByIndex(0x0008, 20)
    SetChrFlags(0x0008, 0x1000)

    @scena.Lambda('lambda_347D')
    def lambda_347D():
        OP_8F(0x00FE, 44040, 16000, -77600, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_347D)

    Sleep(30)

    SetChrChipByIndex(0x0009, 18)
    SetChrFlags(0x0009, 0x1000)

    @scena.Lambda('lambda_34A7')
    def lambda_34A7():
        OP_8F(0x00FE, 42670, 16000, -77000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_34A7)

    @scena.Lambda('lambda_34C2')
    def lambda_34C2():
        OP_8F(0x00FE, 45250, 16000, -78600, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010B, 0x0000, lambda_34C2)

    Sleep(30)

    SetChrChipByIndex(0x000A, 18)
    SetChrFlags(0x000A, 0x1000)

    @scena.Lambda('lambda_34EC')
    def lambda_34EC():
        OP_8F(0x00FE, 42880, 16000, -77510, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_34EC)

    @scena.Lambda('lambda_3507')
    def lambda_3507():
        OP_8F(0x00FE, 45090, 16000, -76480, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_3507)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010B, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000518, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3556'),
        (-1, 'loc_355B'),
    )

    def _loc_3556(): pass

    label('loc_3556')

    OP_B4(0x00)

    Jump('loc_355B')

    def _loc_355B(): pass

    label('loc_355B')

    Return()

# id: 0x0006 offset: 0x355C
@scena.Code('func_06_355C')
def func_06_355C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x010B, 0x00)
    TerminateThread(0x00F9, 0x00)
    Sleep(500)

    OP_6D(38850, 16000, -75750, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(323000, 0)
    OP_6E(386, 0)
    ClearChrFlags(0x0000, 0x0080)
    ClearChrFlags(0x0001, 0x0080)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    SetChrPos(0x0101, 39540, 16000, -77330, 270)
    SetChrPos(0x0102, 39390, 16000, -75710, 270)
    SetChrPos(0x010B, 41200, 16000, -77800, 270)
    SetChrPos(0x00F9, 41070, 16000, -75780, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 37040, 16000, -74990, 0)
    SetChrPos(0x0009, 35310, 16000, -76550, 0)
    SetChrPos(0x000A, 37100, 16000, -78080, 0)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x010B, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x010B, 0)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x0008, 5)
    SetChrChipByIndex(0x0009, 5)
    SetChrChipByIndex(0x000A, 5)
    SetChrSubChip(0x0008, 8)
    SetChrSubChip(0x0009, 10)
    SetChrSubChip(0x000A, 12)
    SetChrFlags(0x0008, 0x0002)
    SetChrFlags(0x0009, 0x0002)
    SetChrFlags(0x000A, 0x0002)
    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x000A, 0x0001)

    @scena.Lambda('lambda_36ED')
    def lambda_36ED():
        OP_6B(2230, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_36ED)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010400183V#1006F#6P好，解决了一批！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x010B, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400184V#1042F#5P很好……\n',
            '就这样一口气突入舰内吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400185V乔丝特，跟着我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0102, 400)

    ChrTalk(
        0x010B,
        (
            '#0090400186V#212F#6P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_37C8')
    def lambda_37C8():
        OP_6D(34850, 16500, -55030, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_37C8)

    @scena.Lambda('lambda_37E0')
    def lambda_37E0():
        OP_67(0, 4920, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_37E0)

    @scena.Lambda('lambda_37F8')
    def lambda_37F8():
        OP_6B(5000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_37F8)

    @scena.Lambda('lambda_3808')
    def lambda_3808():
        OP_6C(326000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_3808)

    @scena.Lambda('lambda_3818')
    def lambda_3818():
        OP_6E(449, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_3818)

    CreateThread(0x0102, 0x01, 0x00, 0x000F)
    Sleep(100)

    CreateThread(0x0101, 0x01, 0x00, 0x000E)
    Sleep(400)

    CreateThread(0x00F9, 0x01, 0x00, 0x0010)
    Sleep(50)

    CreateThread(0x010B, 0x01, 0x00, 0x0011)
    WaitForThreadExit(0x0101, 0x0003)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5404._SN', 147, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x386A
@scena.Code('func_07_386A')
def func_07_386A():
    OP_8C(0x00FE, 90, 400)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 19)

    Return()

# id: 0x0008 offset: 0x3881
@scena.Code('func_08_3881')
def func_08_3881():
    OP_8C(0x00FE, 90, 400)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 6)

    Return()

# id: 0x0009 offset: 0x3898
@scena.Code('func_09_3898')
def func_09_3898():
    @scena.Lambda('lambda_389E')
    def lambda_389E():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_389E')

    DispatchAsync2(0x00FE, 0x0002, lambda_389E)

    Sleep(200)

    OP_99(0x00FE, 0x02, 0x00, 0x0000012C)
    Sleep(200)

    TerminateThread(0x00FE, 0x02)
    SetChrChipByIndex(0x00FE, 6)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000A offset: 0x38D9
@scena.Code('func_0A_38D9')
def func_0A_38D9():
    OP_8C(0x00FE, 270, 0)
    OP_8F(0x00FE, 47430, 16000, -78190, 5000, 0x00)

    Return()

# id: 0x000B offset: 0x38F5
@scena.Code('func_0B_38F5')
def func_0B_38F5():
    OP_8C(0x00FE, 270, 0)
    OP_8F(0x00FE, 47480, 16000, -76830, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x3911
@scena.Code('func_0C_3911')
def func_0C_3911():
    OP_8C(0x00FE, 270, 0)
    OP_8F(0x00FE, 49130, 16000, -79020, 5000, 0x00)

    Return()

# id: 0x000D offset: 0x392D
@scena.Code('func_0D_392D')
def func_0D_392D():
    OP_8C(0x00FE, 270, 0)
    OP_8F(0x00FE, 49190, 16000, -77210, 5000, 0x00)

    Return()

# id: 0x000E offset: 0x3949
@scena.Code('func_0E_3949')
def func_0E_3949():
    OP_8C(0x00FE, 0, 600)
    OP_8E(0x00FE, 37300, 16000, -69520, 7000, 0x00)
    OP_8E(0x00FE, 37300, 16500, -29190, 7000, 0x00)

    Return()

# id: 0x000F offset: 0x3979
@scena.Code('func_0F_3979')
def func_0F_3979():
    OP_8C(0x00FE, 0, 600)
    OP_8E(0x00FE, 38350, 16000, -69530, 7000, 0x00)
    OP_8E(0x00FE, 38350, 16500, -29190, 7000, 0x00)

    Return()

# id: 0x0010 offset: 0x39A9
@scena.Code('func_10_39A9')
def func_10_39A9():
    OP_8C(0x00FE, 0, 600)
    OP_8E(0x00FE, 39800, 16000, -69530, 7000, 0x00)
    OP_8E(0x00FE, 39800, 16500, -29190, 7000, 0x00)

    Return()

# id: 0x0011 offset: 0x39D9
@scena.Code('func_11_39D9')
def func_11_39D9():
    OP_8C(0x00FE, 0, 600)
    OP_8E(0x00FE, 38500, 16000, -69530, 7000, 0x00)
    OP_8E(0x00FE, 38500, 16500, -29190, 7000, 0x00)

    Return()

# id: 0x0012 offset: 0x3A09
@scena.Code('func_12_3A09')
def func_12_3A09():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A2B',
    )

    Call(0, 0x0015)
    Call(0, 0x0017)

    def _loc_3A2B(): pass

    label('loc_3A2B')

    OP_D2(0x00270111, 0x00270121, 0x0A)
    OP_D2(0x00270131, 0x00270141, 0x0B)
    OP_D2(0x000702B5, 0x000702BC, 0x0C)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_3A6E'),
        (0x00000003, 'loc_3A7B'),
        (0x00000004, 'loc_3A88'),
        (0x00000005, 'loc_3A95'),
        (0x00000006, 'loc_3AA2'),
        (0x00000007, 'loc_3AAF'),
        (0x00000008, 'loc_3ABC'),
        (-1, 'loc_3AC9'),
    )

    def _loc_3A6E(): pass

    label('loc_3A6E')

    OP_D2(0x000701D1, 0x000701DD, 0x0D)

    Jump('loc_3AC9')

    def _loc_3A7B(): pass

    label('loc_3A7B')

    OP_D2(0x000701E9, 0x000701F5, 0x0D)

    Jump('loc_3AC9')

    def _loc_3A88(): pass

    label('loc_3A88')

    OP_D2(0x0027036F, 0x0027037C, 0x0D)

    Jump('loc_3AC9')

    def _loc_3A95(): pass

    label('loc_3A95')

    OP_D2(0x00070219, 0x00070225, 0x0D)

    Jump('loc_3AC9')

    def _loc_3AA2(): pass

    label('loc_3AA2')

    OP_D2(0x00070231, 0x0007023D, 0x0D)

    Jump('loc_3AC9')

    def _loc_3AAF(): pass

    label('loc_3AAF')

    OP_D2(0x00070249, 0x00070255, 0x0D)

    Jump('loc_3AC9')

    def _loc_3ABC(): pass

    label('loc_3ABC')

    OP_D2(0x00270177, 0x00270184, 0x0D)

    Jump('loc_3AC9')

    def _loc_3AC9(): pass

    label('loc_3AC9')

    OP_6D(37920, 16500, -35740, 0)
    OP_67(0, 7220, -10000, 0)
    OP_6B(4870, 0)
    OP_6C(335000, 0)
    OP_6E(351, 0)
    SetChrPos(0x0101, 36980, 16500, -28010, 90)
    SetChrPos(0x0102, 38630, 16500, -28010, 90)
    SetChrPos(0x010B, 36980, 16500, -28010, 90)
    SetChrPos(0x00F9, 38630, 16500, -28010, 90)
    SetChrPos(0x000C, 37670, 16500, -28010, 90)
    SetChrPos(0x000B, 38190, 16500, -28010, 90)
    SetChrPos(0x000D, 39700, 16500, -28010, 90)
    SetChrPos(0x000E, 38470, 16500, -28010, 90)
    SetChrPos(0x000F, 36850, 16500, -28010, 90)
    SetChrPos(0x0010, 39500, 16500, -28010, 90)
    SetChrPos(0x0011, 36170, 16500, -28010, 90)
    SetChrPos(0x0012, 37760, 16500, -28010, 90)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 11)
    SetChrChipByIndex(0x010B, 12)
    SetChrChipByIndex(0x00F9, 13)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    SetChrFlags(0x010B, 0x1000)
    SetChrFlags(0x00F9, 0x1000)
    CreateThread(0x0101, 0x01, 0x00, 0x0013)
    FadeIn(1000, 0)
    Sleep(1000)

    @scena.Lambda('lambda_3C15')
    def lambda_3C15():
        OP_6D(35620, 16500, -53400, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3C15)

    @scena.Lambda('lambda_3C2D')
    def lambda_3C2D():
        OP_67(0, 6270, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3C2D)

    @scena.Lambda('lambda_3C45')
    def lambda_3C45():
        OP_6B(5000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_3C45)

    @scena.Lambda('lambda_3C55')
    def lambda_3C55():
        OP_6C(311000, 5000)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_3C55)

    @scena.Lambda('lambda_3C65')
    def lambda_3C65():
        OP_6E(403, 5000)

        ExitThread()

    DispatchAsync(0x010B, 0x0003, lambda_3C65)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5401._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x3C9C
@scena.Code('func_13_3C9C')
def func_13_3C9C():
    CreateThread(0x0101, 0x02, 0x00, 0x0014)
    Sleep(50)

    CreateThread(0x0102, 0x01, 0x00, 0x0014)
    Sleep(400)

    CreateThread(0x010B, 0x01, 0x00, 0x0014)
    Sleep(80)

    CreateThread(0x00F9, 0x01, 0x00, 0x0014)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, 0x0014)
    Sleep(400)

    CreateThread(0x000B, 0x01, 0x00, 0x0014)
    Sleep(500)

    CreateThread(0x000D, 0x01, 0x00, 0x0014)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x00, 0x0014)
    Sleep(300)

    CreateThread(0x000F, 0x01, 0x00, 0x0014)
    Sleep(400)

    CreateThread(0x0010, 0x01, 0x00, 0x0014)
    Sleep(300)

    CreateThread(0x0011, 0x01, 0x00, 0x0014)
    Sleep(200)

    CreateThread(0x0012, 0x01, 0x00, 0x0014)

    Return()

# id: 0x0014 offset: 0x3D28
@scena.Code('func_14_3D28')
def func_14_3D28():
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -80000, 7000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x3D47
@scena.Code('func_15_3D47')
def func_15_3D47():
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
        (0x00000000, 'loc_3DC1'),
        (0x00000001, 'loc_3DC7'),
        (-1, 'loc_3DCD'),
    )

    def _loc_3DC1(): pass

    label('loc_3DC1')

    OP_A2(0x1200)

    Jump('loc_3DCD')

    def _loc_3DC7(): pass

    label('loc_3DC7')

    OP_A2(0x1201)

    Jump('loc_3DCD')

    def _loc_3DCD(): pass

    label('loc_3DCD')

    Return()

# id: 0x0016 offset: 0x3DCE
@scena.Code('func_16_3DCE')
def func_16_3DCE():
    FadeOut(0, 0, -1)
    OP_6D(-344380, 4000, -855980, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
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

# id: 0x0017 offset: 0x3E61
@scena.Code('func_17_3E61')
def func_17_3E61():
    FadeOut(0, 0, -1)
    OP_6D(-344380, 4000, -855980, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
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
            0x000A,
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
