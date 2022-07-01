import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3404_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3404   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '瘦狼瓦鲁特'),
    TXT(0x02, '深渊蠕虫'),
    TXT(0x03, '深渊蠕虫'),
    TXT(0x04, '深渊蠕虫'),
    TXT(0x05, '深渊蠕虫'),
    TXT(0x06, '深渊蠕虫'),
    TXT(0x07, '基库'),
    TXT(0x08, '金'),
    TXT(0x09, '奥利维尔'),
    TXT(0x0A, '科洛丝'),
    TXT(0x0B, '艾丝蒂尔'),
    TXT(0x0C, '金'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3404.x'
    header.mapIndex       = 1
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4EED
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C8,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01CC,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x228
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x228
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x228
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9390,
            triggerZ            = 0,
            triggerY            = 2710,
            triggerRange        = 1600,
            actorX              = 9390,
            actorZ              = 800,
            actorY              = 2710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24C
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_261',
    )

    Event(0, 0x0005)

    def _loc_261(): pass

    label('loc_261')

    ExecExpressionWithValue(
        0x000E,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x273
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x3AF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_288',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_288(): pass

    label('loc_288')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2A5',
    )

    OP_82(0x80, 0x00)
    OP_82(0x83, 0x00)
    OP_82(0x84, 0x00)
    OP_71(0x0001, 0x0004)
    OP_22(0x01C7, 0x00, 0x64)

    Jump('loc_2AE')

    def _loc_2A5(): pass

    label('loc_2A5')

    OP_64(0x00, 0x0001)
    OP_22(0x010B, 0x01, 0x46)

    def _loc_2AE(): pass

    label('loc_2AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2B9',
    )

    OP_64(0x00, 0x0001)

    def _loc_2B9(): pass

    label('loc_2B9')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x3AF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C9',
    )

    Call(0, 0x0004)

    def _loc_2C9(): pass

    label('loc_2C9')

    Return()

# id: 0x0002 offset: 0x2CA
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_2DF(): pass

    label('loc_2DF')

    Return()

# id: 0x0003 offset: 0x2E0
@scena.Code('func_03_2E0')
def func_03_2E0():
    OP_D2(0x00270110, 0x00270120, 0x00)
    OP_D2(0x00270110, 0x00270120, 0x01)
    OP_D2(0x00270110, 0x00270120, 0x02)
    OP_D2(0x00070230, 0x0007023C, 0x03)
    OP_D2(0x00270110, 0x00270120, 0x04)
    OP_D2(0x00270110, 0x00270120, 0x05)
    OP_D2(0x00070218, 0x00070224, 0x06)
    OP_D2(0x00270110, 0x00270120, 0x07)
    OP_D2(0x00270110, 0x00270120, 0x08)
    OP_D2(0x000701D0, 0x000701DC, 0x09)
    OP_D2(0x00270110, 0x00270120, 0x0A)
    OP_D2(0x00270110, 0x00270120, 0x0B)
    OP_D2(0x000701E8, 0x000701F4, 0x0C)
    OP_D2(0x00270110, 0x00270120, 0x0D)
    OP_D2(0x00270110, 0x00270120, 0x0E)
    OP_D2(0x00070200, 0x0007020C, 0x0F)
    OP_D2(0x00270110, 0x00270120, 0x10)
    OP_D2(0x00270110, 0x00270120, 0x11)
    OP_D2(0x00270110, 0x00270120, 0x12)
    OP_D2(0x00270110, 0x00270120, 0x13)
    OP_D2(0x00270110, 0x00270120, 0x14)
    OP_D2(0x002701C6, 0x002701CB, 0x15)
    OP_D2(0x00270110, 0x00270120, 0x16)
    OP_D2(0x00270110, 0x00270120, 0x17)
    OP_D2(0x00270110, 0x00270120, 0x18)
    OP_D2(0x00270110, 0x00270120, 0x19)
    OP_D2(0x00270110, 0x00270120, 0x1A)
    OP_D2(0x00270110, 0x00270120, 0x1B)
    OP_D2(0x00290077, 0x00290079, 0x1C)
    OP_D2(0x0029006E, 0x00290072, 0x1D)
    OP_D2(0x00290070, 0x00290074, 0x1E)
    OP_D2(0x002600A0, 0x002600A5, 0x1F)
    OP_D2(0x00270110, 0x00270120, 0x20)
    OP_D2(0x00270110, 0x00270120, 0x21)
    OP_D2(0x00270110, 0x00270120, 0x22)
    OP_D2(0x00270110, 0x00270120, 0x23)
    OP_D2(0x00270110, 0x00270120, 0x24)
    OP_D2(0x00270110, 0x00270120, 0x25)
    OP_D2(0x00270110, 0x00270120, 0x26)
    OP_D2(0x00270110, 0x00270120, 0x27)

    Return()

# id: 0x0004 offset: 0x471
@scena.Code('func_04_471')
def func_04_471():
    OP_D2(0x00270110, 0x00270120, 0x00)
    OP_D2(0x00270113, 0x00270123, 0x01)
    OP_D2(0x00270114, 0x00270124, 0x02)
    OP_D2(0x00070230, 0x0007023C, 0x03)
    OP_D2(0x00070233, 0x0007023F, 0x04)
    OP_D2(0x00070234, 0x00070240, 0x05)
    OP_D2(0x00070230, 0x0007023C, 0x06)
    OP_D2(0x00070233, 0x0007023F, 0x07)
    OP_D2(0x00070234, 0x00070240, 0x08)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4F3',
    )

    OP_D2(0x00070218, 0x00070224, 0x09)
    OP_D2(0x0007021B, 0x00070227, 0x0A)
    OP_D2(0x0007021C, 0x00070228, 0x0B)

    Jump('loc_511')

    def _loc_4F3(): pass

    label('loc_4F3')

    OP_D2(0x000701D0, 0x000701DC, 0x09)
    OP_D2(0x000701D3, 0x000701DF, 0x0A)
    OP_D2(0x000701D4, 0x000701E0, 0x0B)

    def _loc_511(): pass

    label('loc_511')

    OP_D2(0x000701E8, 0x000701F4, 0x0C)
    OP_D2(0x000701EB, 0x000701F7, 0x0D)
    OP_D2(0x000701EC, 0x000701F8, 0x0E)
    OP_D2(0x00070200, 0x0007020C, 0x0F)
    OP_D2(0x00070203, 0x0007020F, 0x10)
    OP_D2(0x00070204, 0x00070210, 0x11)
    OP_D2(0x000701E9, 0x000701F5, 0x12)
    OP_D2(0x00070041, 0x00070049, 0x13)
    OP_D2(0x00070180, 0x00070184, 0x14)
    OP_D2(0x002701C6, 0x002701CB, 0x15)
    OP_D2(0x0027022A, 0x00270234, 0x16)
    OP_D2(0x0027022B, 0x00270235, 0x17)
    OP_D2(0x0027022C, 0x00270236, 0x18)
    OP_D2(0x00070070, 0x00070078, 0x19)
    OP_D2(0x00070248, 0x00070254, 0x1A)
    OP_D2(0x0007024A, 0x00070256, 0x1B)
    OP_D2(0x00070250, 0x0007025C, 0x1C)
    OP_D2(0x00070250, 0x0007025C, 0x1D)
    OP_D2(0x00270233, 0x0027023D, 0x1E)
    OP_D2(0x002600A0, 0x002600A5, 0x1F)
    OP_D2(0x00260052, 0x00260057, 0x20)
    OP_D2(0x002600A2, 0x002600A7, 0x21)
    OP_D2(0x00270232, 0x0027023C, 0x22)
    OP_D2(0x00060065, 0x0006006A, 0x23)
    OP_D2(0x00070249, 0x00070255, 0x24)
    OP_D2(0x002601A7, 0x002601AC, 0x25)
    OP_D2(0x00070030, 0x00070038, 0x26)
    OP_D2(0x00260068, 0x0026006D, 0x27)

    Return()

# id: 0x0005 offset: 0x62A
@scena.Code('func_05_62A')
def func_05_62A():
    Call(0, 0x0006)
    Call(0, 0x000D)

    Return()

# id: 0x0006 offset: 0x633
@scena.Code('func_06_633')
def func_06_633():
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
        'loc_654',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)

    def _loc_654(): pass

    label('loc_654')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_678',
    )

    LoadEffect(0x00, 'Scraft\\\\sc003_01.eff')

    def _loc_678(): pass

    label('loc_678')

    Call(0, 0x0003)
    OP_6D(-9630, 0, 2800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x0090, 0x00, 0x64)
    SetChrPos(0x0008, 7910, 0, 3440, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 31)
    SetChrPos(0x0101, -14730, 0, 1440, 90)
    SetChrPos(0x00F7, -14750, 0, 2770, 90)
    SetChrPos(0x0107, -15870, 0, 1330, 90)
    SetChrPos(0x00F9, -16200, 0, 2330, 90)

    @scena.Lambda('lambda_0728')
    def lambda_0728():
        OP_8E(0x00FE, -9100, 0, 2270, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0728)

    Sleep(100)

    @scena.Lambda('lambda_0748')
    def lambda_0748():
        OP_8E(0x00FE, -9400, 0, 3600, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0748)

    Sleep(100)

    @scena.Lambda('lambda_0768')
    def lambda_0768():
        OP_8E(0x00FE, -10700, 0, 1820, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0768)

    Sleep(100)

    @scena.Lambda('lambda_0788')
    def lambda_0788():
        OP_8E(0x00FE, -10900, 0, 3250, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0788)

    OP_20(0x000005DC)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x00F9, 0x0001)
    OP_1D(0x6F)

    ChrTalk(
        0x0101,
        (
            '#0010230953V#1020F#5P这、这是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230954V在地面扩散成这个样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230955V#065F能量脉……\n',
            '这个莫非是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0200230956V#6P……呵呵………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0200230957V#6P来得真迟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010230958V#1002F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0948')
    def lambda_0948():
        OP_6D(5590, 0, 2620, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0948)

    @scena.Lambda('lambda_0960')
    def lambda_0960():
        OP_67(0, 2910, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0960)

    @scena.Lambda('lambda_0978')
    def lambda_0978():
        OP_6C(81000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0978)

    @scena.Lambda('lambda_0988')
    def lambda_0988():
        OP_6B(2300, 3000)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0988)

    @scena.Lambda('lambda_0998')
    def lambda_0998():
        OP_6E(474, 3000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_0998)

    Sleep(1000)

    @scena.Lambda('lambda_09AD')
    def lambda_09AD():
        OP_8E(0x00FE, 140, 0, 1240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_09AD)

    Sleep(100)

    @scena.Lambda('lambda_09CD')
    def lambda_09CD():
        OP_8E(0x00FE, -280, -10, 2180, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_09CD)

    Sleep(200)

    @scena.Lambda('lambda_09ED')
    def lambda_09ED():
        OP_8E(0x00FE, -1670, -90, 2660, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_09ED)

    Sleep(100)

    @scena.Lambda('lambda_0A0D')
    def lambda_0A0D():
        OP_8E(0x00FE, -1090, 0, 340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_0A0D)

    Sleep(1500)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0107, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010230959V#1005F#4P戴、戴墨镜的男人……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_AB6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230960V#057F#6P那是……\n',
            '附带『福音』的桩吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEF')

    def _loc_AB6(): pass

    label('loc_AB6')

    ChrTalk(
        0x0103,
        (
            '#0030230961V#022F#6P那是……\n',
            '附带『福音』的桩……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AEF(): pass

    label('loc_AEF')

    NpcTalk(
        0x0008,
        '戴墨镜的男人',
        (
            '#0200230962V#250F#5P哟，小丫头们。\n',
            '远道而来真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230963V让我好好欢迎你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230964V#1005F#4P你……\n',
            '是『噬身之蛇』的人吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '戴墨镜的男人',
        (
            '#0200230965V#252F#5P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C5(0x00, 0x0000, 0x0000, 0x0200, 0x0200, 0x0064, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0200, 0x0200, 0x00FFFFFF, 0x00, 'C_VIS115._CH')
    OP_C6(0x00, 0x00, 125000, 0, 500)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('戴墨镜的男人')

    Talk(
        (
            '#0200230966V#250F执行者ＮＯ．Ⅷ。\n',
            '『瘦狼』瓦鲁特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230967V他们是这样称呼我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    Sleep(250)

    Sleep(500)

    OP_C6(0x00, 0x06, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D0F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230968V#057F#6P果然没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230969V在蔡斯的一连串地震\n',
            '也全都是你搞的鬼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D64')

    def _loc_D0F(): pass

    label('loc_D0F')

    ChrTalk(
        0x0103,
        (
            '#0030230970V#022F#6P果然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230971V在蔡斯的一连串地震\n',
            '全部都是你干的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D64(): pass

    label('loc_D64')

    ChrTalk(
        0x0008,
        (
            '#0200230972V#252F#5P呵呵，这么明显的事\n',
            '就不必特意向我确认了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230973V这个是『结社』开发的\n',
            '为干涉七耀脉的『桩』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230974V本来只是将正下方的\n',
            '七耀脉进行活化的装置……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230975V装上『福音』之后，\n',
            '能够扭曲大范围的七耀脉流动\n',
            '而引起局部性的地震。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230976V也就是，做了一下这样的实验而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EE5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230977V#032F既然你用过去式，\n',
            '代表实验已经结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F23')

    def _loc_EE5(): pass

    label('loc_EE5')

    ChrTalk(
        0x0105,
        (
            '#0060230978V#043F既然你用过去式，\n',
            '代表实验已经结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F23(): pass

    label('loc_F23')

    ChrTalk(
        0x0008,
        (
            '#0200230979V#250F#5P算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230980V本来还想\n',
            '破坏点建筑物\n',
            '显得更华丽些……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230981V但力量还是不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230982V#065F怎、怎么这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230983V如果建筑物崩塌\n',
            '住在里面的人就危险了呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200230984V#252F#5P呵呵，这样才好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230985V一定会有被瓦砾压断手足\n',
            '像猪一样哭喊的\n',
            '人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230986V或许也会有人因脑浆迸裂\n',
            '而当场毙命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230987V小姑娘想不想\n',
            '也尝试一下这种体验？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230988V#069F呜……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0107, 0x00000014, 0x00000000, 0x000001F4, 0x00000FA0)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230989V#1002F#4P这，这家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200230990V#252F#5P嘿嘿，别摆出这么可怕的表情啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230991V我嘛，一向认为有情趣的人生\n',
            '就必然要有适度的刺激才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230992V也就是那种让人手心冒汗的\n',
            '惊险和紧张感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230993V不知道自己何时会死……\n',
            '让自己置身于这种生与死的边缘上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200230994V怎样……不觉得很令人兴奋吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_12C5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230995V#551F#6P哼……你这变态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230996V#057F不过，这下我终于明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230997V你这家伙──\n',
            '是故意引诱我们过来的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1347')

    def _loc_12C5(): pass

    label('loc_12C5')

    ChrTalk(
        0x0103,
        (
            '#0030230998V#025F#6P好扭曲的人生观啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230999V#022F不过，这下终于明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231000V你──\n',
            '是故意引诱我们过来的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1347(): pass

    label('loc_1347')

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010231001V#1020F#4P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1435',
    )

    ChrTalk(
        0x0104,
        (
            '#0040231002V#035F故意在各地留下目击情报……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231003V在要塞发生地震之后\n',
            '亚尔摩的源泉马上就开始沸腾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231004V#030F全部都是故意留下的线索啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D2')

    def _loc_1435(): pass

    label('loc_1435')

    ChrTalk(
        0x0105,
        (
            '#0060231005V#047F故意在各地留下目击情报……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231006V在要塞发生地震之后\n',
            '亚尔摩的源泉马上就开始沸腾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231007V#042F全部都是故意留下的线索啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14D2(): pass

    label('loc_14D2')

    ChrTalk(
        0x0101,
        (
            '#0010231008V#1026F#4P怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200231009V#250F#5P算是说对一半吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231010V那么就马上\n',
            '让我看看吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231011V#252F你们到底能带来多少刺激呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 1)
    Sleep(500)

    SetChrSubChip(0x0008, 2)
    OP_22(0x00BC, 0x00, 0x64)
    OP_20(0x00000000)
    Sleep(500)

    Fade(1000)
    OP_E8(0xDC, 0x05, 0x00, 0x00)
    OP_6D(4130, 0, 3270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(1050, 0)
    OP_6C(45000, 0)
    OP_6E(922, 0)
    SetChrPos(0x0008, 8100, 0, 3250, 270)
    SetChrPos(0x0101, 2029, 0, 1070, 90)
    SetChrPos(0x00F7, 1710, 0, 2520, 90)
    SetChrPos(0x00F9, 260, 0, 2110, 90)
    SetChrPos(0x0107, 690, 0, 550, 90)
    OP_0D()
    OP_22(0x0085, 0x00, 0x64)

    @scena.Lambda('lambda_163B')
    def lambda_163B():
        OP_7C(0x00000000, 0x000000C8, 0x0000012C, 0x00000064)
        Yield()

        Jump('lambda_163B')

    DispatchAsync2(0x0008, 0x0003, lambda_163B)

    OP_6D(2260, 0, 2160, 1500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0009, 150, 800, -3740, 0)
    SetChrPos(0x000A, -3070, 800, 180, 90)
    SetChrPos(0x000B, -2420, 800, 5380, 135)
    SetChrPos(0x000C, 3190, 800, 6030, 180)
    SetChrPos(0x000D, 5440, 800, -1300, 270)
    CreateThread(0x0009, 0x00, 0x00, 0x0007)
    CreateThread(0x000C, 0x00, 0x00, 0x0007)
    Sleep(200)

    CreateThread(0x000A, 0x00, 0x00, 0x0007)
    CreateThread(0x000B, 0x00, 0x00, 0x0007)
    Sleep(200)

    CreateThread(0x000D, 0x00, 0x00, 0x0007)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_1762')
    def lambda_1762():
        OP_8C(0x0107, 225, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1762)

    @scena.Lambda('lambda_1770')
    def lambda_1770():
        OP_8C(0x00F9, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1770)

    Sleep(100)

    @scena.Lambda('lambda_1783')
    def lambda_1783():
        OP_8C(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1783)

    Sleep(100)

    @scena.Lambda('lambda_1796')
    def lambda_1796():
        OP_8C(0x00F7, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1796)

    WaitForThreadExit(0x00F7, 0x0001)
    OP_24(0x0085, 0x5A)
    Sleep(100)

    OP_24(0x0085, 0x50)
    Sleep(100)

    OP_24(0x0085, 0x46)
    Sleep(100)

    OP_24(0x0085, 0x3C)
    Sleep(100)

    OP_24(0x0085, 0x32)
    Sleep(100)

    OP_24(0x0085, 0x28)
    Sleep(100)

    OP_24(0x0085, 0x1E)
    Sleep(100)

    OP_23(0x0085)
    TerminateThread(0x0008, 0x03)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0107, 0)
    SetChrSubChip(0x00F7, 0)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0107, 3)
    OP_1D(0x29)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_181D',
    )

    SetChrChipByIndex(0x0106, 6)

    Jump('loc_1822')

    def _loc_181D(): pass

    label('loc_181D')

    SetChrChipByIndex(0x0103, 9)

    def _loc_1822(): pass

    label('loc_1822')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1837',
    )

    SetChrChipByIndex(0x0104, 12)

    Jump('loc_183C')

    def _loc_1837(): pass

    label('loc_1837')

    SetChrChipByIndex(0x0105, 15)

    def _loc_183C(): pass

    label('loc_183C')

    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070231012V#065F呀！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231013V#1020F#5P这，这些东西是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 31)
    SetChrSubChip(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0200231014V#252F#4P栖息在这附近的蚯蚓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231015V由于七耀脉的活性化\n',
            '而变得这么巨大了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231016V嗯，你们就陪它们尽情玩玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010231017V#1005F#6P开，开什么玩笑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231018V你这胆小鬼！\n',
            '堂堂正正地和我们决胜负啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_19D8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231019V#054F#5P别去管他了！\n',
            '现在得先对付这些东西才行啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A19')

    def _loc_19D8(): pass

    label('loc_19D8')

    ChrTalk(
        0x0103,
        (
            '#0030231020V#024F#5P别管他了！\n',
            '现在得先对付这些东西才行哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A19(): pass

    label('loc_1A19')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A4D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040231021V#530F#5P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A71')

    def _loc_1A4D(): pass

    label('loc_1A4D')

    ChrTalk(
        0x0105,
        (
            '#0060231022V#042F#5P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A71(): pass

    label('loc_1A71')

    CreateThread(0x0009, 0x00, 0x00, 0x0008)
    CreateThread(0x000D, 0x00, 0x00, 0x000C)
    Sleep(30)

    CreateThread(0x000B, 0x00, 0x00, 0x000A)
    Sleep(30)

    CreateThread(0x000A, 0x00, 0x00, 0x0009)
    CreateThread(0x000C, 0x00, 0x00, 0x000B)
    OP_8C(0x0101, 180, 400)
    WaitForThreadExit(0x000D, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    Battle(0x000003AF, 0x00000000, 0x01, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1AE0'),
        (-1, 'loc_1AE5'),
    )

    def _loc_1AE0(): pass

    label('loc_1AE0')

    OP_B4(0x00)

    Jump('loc_1AE5')

    def _loc_1AE5(): pass

    label('loc_1AE5')

    Return()

# id: 0x0007 offset: 0x1AE6
@scena.Code('func_07_1AE6')
def func_07_1AE6():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
    SetChrChipByIndex(0x00FE, 29)
    SetChrSubChip(0x00FE, 0)
    CreateThread(0x00FE, 0x01, 0x00, 0x0002)

    Return()

# id: 0x0008 offset: 0x1B0B
@scena.Code('func_08_1B0B')
def func_08_1B0B():
    TerminateThread(0x00FE, 0x01)
    SetChrChipByIndex(0x00FE, 30)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1B1F')
    def lambda_1B1F():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1B1F)

    Sleep(200)

    OP_8F(0x00FE, 450, 800, -1000, 6000, 0x00)

    Return()

# id: 0x0009 offset: 0x1B43
@scena.Code('func_09_1B43')
def func_09_1B43():
    TerminateThread(0x00FE, 0x01)
    SetChrChipByIndex(0x00FE, 30)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1B57')
    def lambda_1B57():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1B57)

    Sleep(200)

    OP_8F(0x00FE, -1340, 800, 570, 6000, 0x00)

    Return()

# id: 0x000A offset: 0x1B7B
@scena.Code('func_0A_1B7B')
def func_0A_1B7B():
    TerminateThread(0x00FE, 0x01)
    SetChrChipByIndex(0x00FE, 30)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1B8F')
    def lambda_1B8F():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1B8F)

    Sleep(200)

    OP_8F(0x00FE, -420, 800, 3770, 6000, 0x00)

    Return()

# id: 0x000B offset: 0x1BB3
@scena.Code('func_0B_1BB3')
def func_0B_1BB3():
    TerminateThread(0x00FE, 0x01)
    SetChrChipByIndex(0x00FE, 30)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1BC7')
    def lambda_1BC7():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1BC7)

    Sleep(200)

    OP_8F(0x00FE, 2350, 800, 4059, 6000, 0x00)

    Return()

# id: 0x000C offset: 0x1BEB
@scena.Code('func_0C_1BEB')
def func_0C_1BEB():
    TerminateThread(0x00FE, 0x01)
    SetChrChipByIndex(0x00FE, 30)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1BFF')
    def lambda_1BFF():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1BFF)

    Sleep(200)

    OP_8F(0x00FE, 3440, 800, 110, 6000, 0x00)

    Return()

# id: 0x000D offset: 0x1C23
@scena.Code('func_0D_1C23')
def func_0D_1C23():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_6D(3700, 0, 3240, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(53000, 0)
    OP_6E(474, 0)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    OP_22(0x0090, 0x00, 0x64)
    SetChrPos(0x0008, 8100, 0, 3250, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 31)
    SetChrPos(0x0101, 2029, 0, 1070, 180)
    SetChrPos(0x00F7, 1710, 0, 2520, 0)
    SetChrPos(0x00F9, 260, 0, 2110, 270)
    SetChrPos(0x0107, 690, 0, 550, 180)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0107, 0)
    SetChrSubChip(0x00F7, 0)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0107, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1D1B',
    )

    SetChrChipByIndex(0x0106, 9)

    Jump('loc_1D20')

    def _loc_1D1B(): pass

    label('loc_1D1B')

    SetChrChipByIndex(0x0103, 9)

    def _loc_1D20(): pass

    label('loc_1D20')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D35',
    )

    SetChrChipByIndex(0x0104, 12)

    Jump('loc_1D3A')

    def _loc_1D35(): pass

    label('loc_1D35')

    SetChrChipByIndex(0x0105, 15)

    def _loc_1D3A(): pass

    label('loc_1D3A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D5E',
    )

    LoadEffect(0x00, 'Scraft\\\\sc003_01.eff')

    def _loc_1D5E(): pass

    label('loc_1D5E')

    LoadEffect(0x01, 'battle\\\\damage0.eff')
    LoadEffect(0x02, 'Scraft\\\\sc006_17.eff')
    LoadEffect(0x03, 'Scraft\\\\sc006_16.eff')
    LoadEffect(0x04, 'Scraft\\\\sc007_05.eff')
    LoadEffect(0x05, 'Scraft\\\\sc007_06.eff')
    LoadEffect(0x06, 'Scraft\\sc000_00.eff')
    LoadEffect(0x07, 'Scraft\\sc000_10.eff')
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010231023V#1025F#5P总算赶走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231024V#561F吓、吓死了～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EA3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040231025V#034F#6P哎呀呀……\n',
            '真是一点也不美丽的敌人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ED4')

    def _loc_1EA3(): pass

    label('loc_1EA3')

    ChrTalk(
        0x0105,
        (
            '#0060231026V#042F#6P呼……\n',
            '好麻烦的对手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ED4(): pass

    label('loc_1ED4')

    ChrTalk(
        0x0008,
        (
            '#0200231027V#250F#4P嗯～看来稍微出乎\n',
            '我的预料之外……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231028V还以为会更强一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F37')
    def lambda_1F37():
        OP_6D(5390, 0, 3650, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F37)

    OP_8C(0x0101, 90, 400)
    OP_8C(0x00F7, 90, 400)
    OP_8C(0x00F9, 90, 400)
    OP_8C(0x0107, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1FD1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231029V#555F#6P哼，别小看我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231030V这种程度的魔兽\n',
            '以前不知打倒过多少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202C')

    def _loc_1FD1(): pass

    label('loc_1FD1')

    ChrTalk(
        0x0103,
        (
            '#0030231031V#022F#6P请别小看我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231032V这种程度的魔兽\n',
            '以前不知打倒过多少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_202C(): pass

    label('loc_202C')

    ChrTalk(
        0x0008,
        (
            '#0200231033V#254F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231034V……真是的，简直不知该说什么好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231035V没想到你们\n',
            '居然如此天真。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_20DC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231036V#052F#6P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2100')

    def _loc_20DC(): pass

    label('loc_20DC')

    ChrTalk(
        0x0103,
        (
            '#0030231037V#023F#6P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2100(): pass

    label('loc_2100')

    Fade(500)

    @scena.Lambda('lambda_210B')
    def lambda_210B():
        OP_6B(2100, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_210B)

    SetChrChipByIndex(0x0008, 23)
    SetChrSubChip(0x0008, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200231038V#258F一群白痴……\n',
            '小看我的是你们才对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x00, 0x00, 0x0018)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0003)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x00F7, 0x0003)
    WaitForThreadExit(0x00F9, 0x0003)
    WaitForThreadExit(0x0107, 0x0003)
    Sleep(600)

    CreateThread(0x00F7, 0x01, 0x00, 0x000E)
    Sleep(200)

    CreateThread(0x0101, 0x01, 0x00, 0x000F)
    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, 0x0011)
    Sleep(200)

    CreateThread(0x0107, 0x01, 0x00, 0x0010)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0107, 0x0001)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_99(0x0008, 0x1E, 0x1C, 0x000003E8)
    Fade(500)
    SetChrFlags(0x0008, 0x0100)
    ClearChrFlags(0x0008, 0x0002)

    ExecExpressionWithValue(
        0x0008,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 24)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0008, 3240, 0, 1820, 225)

    @scena.Lambda('lambda_2228')
    def lambda_2228():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2228)

    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200231047V#254F……混帐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_225D')
    def lambda_225D():
        OP_6D(4130, 0, 3270, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_225D)

    @scena.Lambda('lambda_2275')
    def lambda_2275():
        OP_67(0, 5500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2275)

    @scena.Lambda('lambda_228D')
    def lambda_228D():
        OP_6B(2000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_228D)

    @scena.Lambda('lambda_229D')
    def lambda_229D():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_229D)

    @scena.Lambda('lambda_22AD')
    def lambda_22AD():
        OP_6E(474, 3000)

        ExitThread()

    DispatchAsync(0x0002, 0x0002, lambda_22AD)

    CreateThread(0x0008, 0x01, 0x00, 0x0012)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0001)
    Fade(250)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 31)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0200231048V#254F真是的，莱维那家伙\n',
            '真会跟我胡扯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231049V什～么除『剑圣』以外\n',
            '可能还有一些棘手的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231050V不过是些乳臭未干的小鬼嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23AB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231051V#057F#5P可恶……不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D7')

    def _loc_23AB(): pass

    label('loc_23AB')

    ChrTalk(
        0x0103,
        (
            '#0030231052V#522F#5P可恶……怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23D7(): pass

    label('loc_23D7')

    ChrTalk(
        0x0008,
        (
            '#0200231053V#252F哼，既然这样也没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231054V干脆跟教授直接谈判，\n',
            '去收拾那漆黑小子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231055V那样的话，大概\n',
            '多少能找到点刺激吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231056V#1020F#6P！！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231057V#1005F等……等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_24B5')
    def lambda_24B5():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_24B5')

    DispatchAsync2(0x0101, 0x0003, lambda_24B5)

    Sleep(500)

    OP_99(0x0101, 0x03, 0x00, 0x0000012C)
    Sleep(500)

    TerminateThread(0x0101, 0x03)
    SetChrFlags(0x0008, 0x0020)
    OP_8C(0x0008, 225, 400)
    ClearChrFlags(0x0008, 0x0020)
    ClearChrFlags(0x0101, 0x0800)

    ChrTalk(
        0x0008,
        (
            '#0200231058V#250F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231059V#1005F#6P你这墨镜男……\n',
            '给我适可而止吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231060V漆黑小子什么的…\n',
            '如果说的是约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231061V我绝对……\n',
            '绝对不容许你乱来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231062V#065F#5P艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200231063V#250F受了我一击\n',
            '居然还能站得住，的确值得夸奖……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231064V不过还是算了吧。\n',
            '连膝盖都在颤抖哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231065V#1022F#6P那、那又怎么样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231066V我绝对……\n',
            '要找到约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010231067V#1005F#6P我绝不会让你们\n',
            '阻挠我！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2721',
    )

    ChrTalk(
        0x0104,
        (
            '#0040231068V#032F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2747')

    def _loc_2721(): pass

    label('loc_2721')

    ChrTalk(
        0x0105,
        (
            '#0060231069V#043F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2747(): pass

    label('loc_2747')

    @scena.Lambda('lambda_274D')
    def lambda_274D():
        OP_6D(2990, 0, 690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_274D)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 21)
    OP_8E(0x0008, 3740, 0, 310, 2000, 0x00)
    OP_8C(0x0008, 270, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 31)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0200231070V#250F#2P……话说在先，\n',
            '我可不会对女人或小孩手软的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231071V身为武术家，在面对敌人时，\n',
            '你应该早已有所觉悟吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231072V#1005F#6P当然……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231073V有本事的话\n',
            '就尽管动手吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200231074V#252F#2P哼哼，真有种……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    @scena.Lambda('lambda_28A2')
    def lambda_28A2():
        OP_6B(1800, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_28A2)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 23)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200231075V#250F#2P看在你这胆量的份上\n',
            '我就一击了结你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231076V#1002F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x000000C8, 1600, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070231077V#069F#7P不要不要！\n',
            '艾丝蒂尔姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_29AE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231078V#054F#5P艾丝蒂尔、快逃啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DC')

    def _loc_29AE(): pass

    label('loc_29AE')

    ChrTalk(
        0x0103,
        (
            '#0030231079V#024F#5P艾丝蒂尔、快逃啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29DC(): pass

    label('loc_29DC')

    ChrTalk(
        0x0008,
        (
            '#0200231080V#250F#2P──去死吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000000)
    OP_E8(0xDC, 0x05, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B3A',
    )

    OP_22(0x0197, 0x00, 0x64)
    OP_22(0x008C, 0x00, 0x64)
    SetChrPos(0x000E, -11220, 3000, 3760, 90)
    SetChrFlags(0x000E, 0x0040)
    OP_7D(0x00, 0x000E, 0x0032, 0x01F4)
    OP_6D(-3050, 0, 3540, 800)
    ClearChrFlags(0x000E, 0x0080)
    CreateThread(0x000E, 0x01, 0x00, 0x0015)

    @scena.Lambda('lambda_2A64')
    def lambda_2A64():
        OP_6D(3230, 0, 1550, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_2A64)

    @scena.Lambda('lambda_2A7C')
    def lambda_2A7C():
        OP_6B(2000, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2A7C)

    @scena.Lambda('lambda_2A8C')
    def lambda_2A8C():
        OP_8E(0x000E, 3740, 0, 310, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2A8C)

    Sleep(500)

    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_2AB1')
    def lambda_2AB1():
        OP_96(0x0008, 0x000016BC, 0x00000000, 0x00000366, 0x0000012C, 0x00003A98)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2AB1)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 22)

    @scena.Lambda('lambda_2AD9')
    def lambda_2AD9():
        ChrTurnDirection(0x0008, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2AD9)

    OP_7D(0x01, 0x000E, 0x0000, 0x0000)

    @scena.Lambda('lambda_2AEF')
    def lambda_2AEF():
        OP_8E(0x000E, 17460, 4000, -2510, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2AEF)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200231081V#254F#2P唔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0002)
    TerminateThread(0x000E, 0x01)
    SetChrFlags(0x000E, 0x0080)

    Jump('loc_2BC2')

    def _loc_2B3A(): pass

    label('loc_2B3A')

    @scena.Lambda('lambda_2B40')
    def lambda_2B40():
        OP_6B(2000, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2B40)

    PlayEffect(0x00, 0xFF, 0x00FF, -6020, 1000, 400, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_96(0x0008, 0x000016BC, 0x00000000, 0x00000366, 0x0000012C, 0x00003A98)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0200231081V#254F#2P唔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BC2(): pass

    label('loc_2BC2')

    ChrTalk(
        0x0101,
        (
            '#0010211050V#1004F#6P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x2C)
    Fade(400)
    OP_6D(-200, 0, -400, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(78000, 0)
    OP_6E(474, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7D(0x00, 0x000F, 0x0032, 0x012C)
    SetChrPos(0x000F, -10320, 0, -160, 90)
    ClearChrFlags(0x000F, 0x0080)
    SetChrChipByIndex(0x000F, 36)
    SetChrSubChip(0x000F, 0)

    NpcTalk(
        0x000F,
        '男人的声音',
        (
            '#0080231084V#10A#5P嗬啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_2C91')
    def lambda_2C91():
        OP_8E(0x00FE, -5780, -70, 390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2C91)

    WaitForThreadExit(0x000F, 0x0001)

    @scena.Lambda('lambda_2CB1')
    def lambda_2CB1():
        OP_6D(3500, 0, 400, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2CB1)

    SetChrFlags(0x000F, 0x0004)
    SetChrFlags(0x000F, 0x0002)
    SetChrFlags(0x000F, 0x0020)
    SetChrChipByIndex(0x000F, 28)
    SetChrSubChip(0x000F, 32)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_2CE7')
    def lambda_2CE7():
        OP_96(0x00FE, 0xFFFFFB78, 0xFFFFFF9C, 0xFFFFF5C4, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2CE7)

    WaitForThreadExit(0x000F, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x000F, 33)
    SetChrSubChip(0x000F, 15)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_2D1E')
    def lambda_2D1E():
        OP_96(0x00FE, 0x00000226, 0xFFFFFF9C, 0x000004C4, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2D1E)

    WaitForThreadExit(0x000F, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_2D46')
    def lambda_2D46():
        OP_6D(5000, 0, 1360, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D46)

    @scena.Lambda('lambda_2D5E')
    def lambda_2D5E():
        OP_67(0, 4500, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D5E)

    @scena.Lambda('lambda_2D76')
    def lambda_2D76():
        OP_6B(1600, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2D76)

    @scena.Lambda('lambda_2D86')
    def lambda_2D86():
        OP_6C(45000, 500)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_2D86)

    SetChrFlags(0x000F, 0x0004)
    SetChrFlags(0x000F, 0x0002)
    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000F, 33)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_2DAF')
    def lambda_2DAF():
        OP_96(0x000F, 0x000010FE, 0x000001F4, 0x000003C0, 0x000007D0, 0x00001B58)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_2DAF)

    OP_99(0x000F, 0x00, 0x03, 0x00000DAC)
    SetChrSubChip(0x000F, 3)
    SetChrChipByIndex(0x000F, 33)
    OP_7D(0x01, 0x000F, 0x0000, 0x0000)
    CreateThread(0x0101, 0x03, 0x00, 0x001E)
    Sleep(200)

    CreateThread(0x000F, 0x00, 0x00, 0x001D)
    WaitForThreadExit(0x000F, 0x0000)

    @scena.Lambda('lambda_2E00')
    def lambda_2E00():
        OP_6B(2000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E00)

    @scena.Lambda('lambda_2E10')
    def lambda_2E10():
        OP_6D(5330, 0, 1510, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E10)

    @scena.Lambda('lambda_2E28')
    def lambda_2E28():
        OP_67(0, 5500, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E28)

    ClearChrFlags(0x000F, 0x0004)

    @scena.Lambda('lambda_2E45')
    def lambda_2E45():
        OP_96(0x00FE, 0x00000C26, 0x00000000, 0x00000154, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2E45)

    @scena.Lambda('lambda_2E63')
    def lambda_2E63():
        OP_99(0x000F, 0x13, 0x17, 0x000007D0)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_2E63)

    WaitForThreadExit(0x000F, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x000F, 0x0002)
    Sleep(500)

    NpcTalk(
        0x000F,
        '东方风格的巨汉',
        (
            '#0080231085V#6P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FC1',
    )

    SetChrPos(0x0011, -5100, 0, -1100, 90)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x000E, 7850, 4000, 9650, 90)
    ClearChrFlags(0x000E, 0x0080)

    NpcTalk(
        0x0011,
        '女孩的声音',
        (
            '#0060231086V#2P呼……\n',
            '看来赶上了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrChipByIndex(0x0011, 19)
    CreateThread(0x000E, 0x00, 0x00, 0x0015)
    CreateThread(0x000E, 0x01, 0x00, 0x0016)
    OP_8F(0x0011, 1800, 0, 1300, 5000, 0x00)
    SetChrSubChip(0x0011, 3)
    SetChrChipByIndex(0x0011, 35)
    WaitForThreadExit(0x000E, 0x0001)
    Fade(250)
    SetChrFlags(0x000E, 0x0080)
    SetChrSubChip(0x0011, 1)
    SetChrChipByIndex(0x0011, 35)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010231087V#1004F#6P科洛丝！\n',
            '还有……金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3093')

    def _loc_2FC1(): pass

    label('loc_2FC1')

    SetChrPos(0x0010, -4120, 0, -400, 90)
    ClearChrFlags(0x0010, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2FE3',
    )

    SetChrFlags(0x0010, 0x8000)

    def _loc_2FE3(): pass

    label('loc_2FE3')

    NpcTalk(
        0x0010,
        '青年的声音',
        (
            '#0040231088V#2P呼……\n',
            '看来赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrChipByIndex(0x0010, 18)
    OP_8F(0x0010, 1800, 0, 1300, 5000, 0x00)
    OP_8C(0x0010, 90, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3047',
    )

    ClearChrFlags(0x0010, 0x8000)

    def _loc_3047(): pass

    label('loc_3047')

    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x0010, 12)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010231089V#1004F#6P奥利维尔！\n',
            '还有……金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3093(): pass

    label('loc_3093')

    ChrTalk(
        0x000F,
        (
            '#0080231090V#070F#5P哟，艾丝蒂尔。\n',
            '真是好久不见了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231091V原本打算早点赶来的，\n',
            '但那边的工作一直拖延……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231092V不过，看来总算赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3170',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231093V#556F#5P真是的……算准了\n',
            '时机才出现啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A7')

    def _loc_3170(): pass

    label('loc_3170')

    ChrTalk(
        0x0103,
        (
            '#0030231094V#524F#5P呵呵……算准了\n',
            '时机才过来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31A7(): pass

    label('loc_31A7')

    ChrTalk(
        0x0008,
        (
            '#0200231095V#257F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231096V莱维的报告里\n',
            '卡尔瓦德的Ａ级游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231097V#251F金，指的就是你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0080231098V#074F#6P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231099V#072F没想到会在这种地方\n',
            '再度碰到你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231100V你什么时候\n',
            '加入到『结社』了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200231101V#253F呵，在那之后\n',
            '我很快就被网罗了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231102V每天都过得\n',
            '相当刺激哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0080231103V#077F#6P说什么傻话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231104V#076F你到底知不知道\n',
            '自己在做什么啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231105V这样做\n',
            '师父什么时候才能瞑目……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200231106V#255F喂喂，别说那些漂亮话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231107V你应该知道才对。\n',
            '我选择了什么样的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231108V#253F再胡说八道……就杀了你哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0080231109V#072F#6P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231110V#075F那么……\n',
            '你知道吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231111V雾香她人在蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0200231112V#255F什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0080231113V#072F#6P听说从两年前开始\n',
            '就做了协会的接待员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231114V在这之前\n',
            '似乎是在大陆各地巡游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200231115V#256F……啧………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231116V没想到会在利贝尔\n',
            '这么远的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231117V#257F那白痴，想什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0080231118V#074F#6P谁知道，我也不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231119V#070F不过，那家伙一定\n',
            '很想见你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231120V『结社』的事姑且不论\n',
            '好歹去露个脸如何……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 34)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_3656')
    def lambda_3656():
        OP_99(0x0008, 0x00, 0x02, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3656)

    WaitForThreadExit(0x0008, 0x0002)

    @scena.Lambda('lambda_366B')
    def lambda_366B():
        OP_6D(3710, 0, 400, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_366B)

    @scena.Lambda('lambda_3683')
    def lambda_3683():
        OP_67(0, 4500, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3683)

    @scena.Lambda('lambda_369B')
    def lambda_369B():
        OP_6B(1600, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_369B)

    ClearChrFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_36B0')
    def lambda_36B0():
        OP_96(0x0008, 0x00001108, 0x000004B0, 0x000000A0, 0x00000578, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_36B0)

    OP_22(0x0084, 0x00, 0x64)

    @scena.Lambda('lambda_36D3')
    def lambda_36D3():
        OP_99(0x0008, 0x02, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_36D3)

    WaitForThreadExit(0x0008, 0x0002)
    OP_7C(0x00000064, 0x00000000, 0x00001388, 0x000003E8)
    PlayEffect(0x07, 0xFF, 0x000F, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    ClearChrFlags(0x000F, 0x0002)
    ClearChrFlags(0x000F, 0x0020)
    OP_8C(0x000F, 90, 0)
    SetChrChipByIndex(0x000F, 27)
    SetChrSubChip(0x000F, 6)

    @scena.Lambda('lambda_3749')
    def lambda_3749():
        OP_8F(0x00FE, 3110, 0, 840, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_3749)

    @scena.Lambda('lambda_3764')
    def lambda_3764():
        OP_9E(0x000F, 0x00000028, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_3764)

    Sleep(200)

    @scena.Lambda('lambda_3783')
    def lambda_3783():
        OP_99(0x0008, 0x05, 0x0C, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3783)

    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x000F,
        (
            '#0080231121V#077F#6P啧……',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0008, 0x0002)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37EF',
    )

    SetChrFlags(0x0011, 0x0020)
    OP_8C(0x0011, 135, 400)
    ClearChrFlags(0x0011, 0x0020)

    Jump('loc_37F6')

    def _loc_37EF(): pass

    label('loc_37EF')

    OP_8C(0x0010, 135, 400)

    def _loc_37F6(): pass

    label('loc_37F6')

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0008, 31)
    SetChrSubChip(0x0008, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0200231122V#254F#2P我不是说了\n',
            '再胡说八道就杀了你吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_384A')
    def lambda_384A():
        OP_6D(5700, 0, 2200, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_384A)

    @scena.Lambda('lambda_3862')
    def lambda_3862():
        OP_67(0, 5500, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3862)

    @scena.Lambda('lambda_387A')
    def lambda_387A():
        OP_6B(2000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_387A)

    Sleep(100)

    OP_8C(0x0008, 225, 0)
    SetChrChipByIndex(0x0008, 32)
    SetChrSubChip(0x0008, 0)
    OP_22(0x023B, 0x00, 0x64)
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)
    OP_96(0x0008, 0x00001EB4, 0x00000000, 0x00000B22, 0x00000190, 0x00001770)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    SetChrSubChip(0x0008, 1)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 31)
    SetChrChipByIndex(0x000F, 26)
    SetChrSubChip(0x000F, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3900',
    )

    SetChrFlags(0x0011, 0x0020)
    OP_8C(0x0011, 90, 400)
    ClearChrFlags(0x0011, 0x0020)

    Jump('loc_3907')

    def _loc_3900(): pass

    label('loc_3900')

    OP_8C(0x0010, 90, 400)

    def _loc_3907(): pass

    label('loc_3907')

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200231123V#250F算了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231124V雾香的事姑且不论，\n',
            '能碰到你已经够幸运的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231125V此次的计划……\n',
            '就尽情享受吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_399F')
    def lambda_399F():
        OP_6D(6620, 0, 2060, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_399F)

    SetChrFlags(0x0008, 0x0020)
    OP_8C(0x0008, 90, 400)
    ClearChrFlags(0x0008, 0x0020)
    Sleep(500)

    OP_22(0x0082, 0x00, 0x64)
    OP_71(0x0001, 0x0004)
    Sleep(1000)

    OP_22(0x0064, 0x00, 0x64)
    OP_22(0x0083, 0x00, 0x64)
    Sleep(500)

    OP_22(0x009A, 0x00, 0x64)
    Sleep(500)

    Fade(1000)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0001)
    OP_79(0x02, 0x0001)
    OP_79(0x03, 0x0001)
    OP_79(0x04, 0x0001)
    OP_7B()
    OP_82(0x80, 0x00)
    OP_82(0x83, 0x02)
    OP_82(0x84, 0x02)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_24(0x0090, 0x5A)
    Sleep(500)

    OP_24(0x0090, 0x50)
    Sleep(500)

    OP_24(0x0090, 0x46)
    Sleep(500)

    OP_24(0x0090, 0x3C)
    Sleep(250)

    OP_24(0x0090, 0x32)
    Sleep(250)

    OP_24(0x0090, 0x28)
    Sleep(250)

    OP_24(0x0090, 0x1E)
    Sleep(150)

    OP_24(0x0090, 0x14)
    Sleep(50)

    OP_24(0x0090, 0x0A)
    Sleep(50)

    OP_23(0x0090)

    ChrTalk(
        0x000F,
        (
            '#0080231126V#076F#6P喂、瓦鲁特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0020)
    OP_8C(0x0008, 225, 400)
    ClearChrFlags(0x0008, 0x0020)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200231127V#252F#2P哼哼，下次见面之前\n',
            '好好锻炼功夫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200231128V再见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0020)
    OP_8C(0x0008, 270, 400)
    ClearChrFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_3B46')
    def lambda_3B46():
        OP_6D(3970, 0, 2280, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3B46)

    @scena.Lambda('lambda_3B5E')
    def lambda_3B5E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3B5E')

    DispatchAsync2(0x0101, 0x0003, lambda_3B5E)

    @scena.Lambda('lambda_3B6F')
    def lambda_3B6F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3B6F')

    DispatchAsync2(0x000F, 0x0003, lambda_3B6F)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BA0',
    )

    SetChrFlags(0x0011, 0x0020)

    @scena.Lambda('lambda_3B92')
    def lambda_3B92():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3B92')

    DispatchAsync2(0x0011, 0x0003, lambda_3B92)

    Jump('loc_3BB1')

    def _loc_3BA0(): pass

    label('loc_3BA0')

    @scena.Lambda('lambda_3BA6')
    def lambda_3BA6():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3BA6')

    DispatchAsync2(0x0010, 0x0003, lambda_3BA6)

    def _loc_3BB1(): pass

    label('loc_3BB1')

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 21)

    @scena.Lambda('lambda_3BC1')
    def lambda_3BC1():
        OP_8F(0x0008, -9000, 0, 4000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3BC1)

    Sleep(1500)

    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)
    Sleep(1000)

    TerminateThread(0x0011, 0x03)
    TerminateThread(0x0010, 0x03)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C28',
    )

    @scena.Lambda('lambda_3C1D')
    def lambda_3C1D():
        OP_8C(0x00FE, 325, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_3C1D)

    Jump('loc_3C36')

    def _loc_3C28(): pass

    label('loc_3C28')

    @scena.Lambda('lambda_3C2E')
    def lambda_3C2E():
        OP_8C(0x00FE, 325, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_3C2E)

    def _loc_3C36(): pass

    label('loc_3C36')

    ChrTalk(
        0x000F,
        (
            '#0080231129V#076F#3S#5P瓦鲁特！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C63')
    def lambda_3C63():
        OP_6D(-500, 0, 2000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C63)

    @scena.Lambda('lambda_3C7B')
    def lambda_3C7B():
        OP_67(0, 6500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3C7B)

    @scena.Lambda('lambda_3C93')
    def lambda_3C93():
        OP_6C(33000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_3C93)

    TerminateThread(0x000F, 0x03)
    SetChrChipByIndex(0x000F, 36)
    SetChrSubChip(0x000F, 0)
    OP_8E(0x000F, 2530, 0, 3980, 4000, 0x00)
    OP_20(0x00000BB8)
    OP_8E(0x000F, -800, -130, 3730, 4000, 0x00)
    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000F, 25)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0011, 0x03)
    TerminateThread(0x0010, 0x03)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0080)
    Sleep(500)

    WaitForThreadExit(0x0008, 0x0003)

    ChrTalk(
        0x000F,
        (
            '#0080231130V#072F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, 0x0013)
    Sleep(800)

    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    CreateThread(0x00F9, 0x01, 0x00, 0x0013)
    Sleep(800)

    CreateThread(0x0107, 0x01, 0x00, 0x0013)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D75',
    )

    Jump('loc_3D7F')

    def _loc_3D75(): pass

    label('loc_3D75')

    SetChrChipByIndex(0x0010, 38)
    SetChrSubChip(0x0010, 0)

    def _loc_3D7F(): pass

    label('loc_3D7F')

    WaitForThreadExit(0x0107, 0x0001)
    OP_8C(0x0101, 325, 0)

    ChrTalk(
        0x0101,
        (
            '#0010231131V#1025F#6P嗯……\n',
            '谢谢你救了我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231132V但是，为什么\n',
            '金先生你们会在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1D(0x01)

    @scena.Lambda('lambda_3DF2')
    def lambda_3DF2():
        OP_6D(200, 0, 2700, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3DF2)

    @scena.Lambda('lambda_3E0A')
    def lambda_3E0A():
        OP_6C(5000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E0A)

    Sleep(500)

    ChrTurnDirection(0x000F, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000F,
        (
            '#0080231133V#070F#5P我跑去蔡斯支部的时候，\n',
            '突然就被雾香催赶过来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231134V叫我赶快到亚尔摩\n',
            '帮助你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EDD',
    )

    OP_8C(0x0011, 180, 400)

    ChrTalk(
        0x0011,
        (
            '#0060231135V#041F#5P于是我也\n',
            '跟着过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F17')

    def _loc_3EDD(): pass

    label('loc_3EDD')

    OP_8C(0x0010, 180, 400)

    ChrTalk(
        0x0010,
        (
            '#0040231136V#031F#5P呼，于是我也\n',
            '陪着过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F17(): pass

    label('loc_3F17')

    ChrTalk(
        0x0101,
        (
            '#0010231137V#1025F#6P是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231138V#1016F谢谢。\n',
            '真的帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3FC1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231139V#053F#6P话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231140V#555F你和那家伙\n',
            '是什么关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4015')

    def _loc_3FC1(): pass

    label('loc_3FC1')

    ChrTalk(
        0x0103,
        (
            '#0030231141V#026F#6P话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231142V#022F金先生和那个人\n',
            '是什么关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4015(): pass

    label('loc_4015')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4038',
    )

    SetChrFlags(0x0011, 0x0020)

    @scena.Lambda('lambda_402D')
    def lambda_402D():
        ChrTurnDirection(0x0011, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_402D)

    Jump('loc_4046')

    def _loc_4038(): pass

    label('loc_4038')

    @scena.Lambda('lambda_403E')
    def lambda_403E():
        ChrTurnDirection(0x0010, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_403E)

    def _loc_4046(): pass

    label('loc_4046')

    ChrTalk(
        0x000F,
        (
            '#0080231143V#074F#5P……嗯，以前的朋友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231144V#070F详情等离开这里\n',
            '回到旅馆后洗个澡再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231145V龙脉的混乱平息之后\n',
            '温泉马上也恢复原样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '返回亚尔摩的艾丝蒂尔一行人\n',
            '在红叶亭的澡堂暖和身体之后\n',
            '决定返回蔡斯支部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    SetMapFlags(0x02000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x4167
@scena.Code('func_0E_4167')
def func_0E_4167():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4180',
    )

    SetChrFlags(0x0106, 0x8000)
    SetChrSubChip(0x0106, 0)
    SetChrChipByIndex(0x0106, 11)

    Jump('loc_418A')

    def _loc_4180(): pass

    label('loc_4180')

    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0103, 11)

    def _loc_418A(): pass

    label('loc_418A')

    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

    Return()

# id: 0x000F offset: 0x4199
@scena.Code('func_0F_4199')
def func_0F_4199():
    SetChrFlags(0x0101, 0x0800)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 2)
    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

    Return()

# id: 0x0010 offset: 0x41B7
@scena.Code('func_10_41B7')
def func_10_41B7():
    SetChrSubChip(0x0107, 0)
    SetChrChipByIndex(0x0107, 5)
    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

    Return()

# id: 0x0011 offset: 0x41D0
@scena.Code('func_11_41D0')
def func_11_41D0():
    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41EF',
    )

    SetChrFlags(0x0104, 0x8000)
    SetChrSubChip(0x0104, 0)
    SetChrChipByIndex(0x0104, 14)

    Jump('loc_41FE')

    def _loc_41EF(): pass

    label('loc_41EF')

    SetChrFlags(0x0105, 0x8000)
    SetChrSubChip(0x0105, 0)
    SetChrChipByIndex(0x0105, 17)

    def _loc_41FE(): pass

    label('loc_41FE')

    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

    Return()

# id: 0x0012 offset: 0x420D
@scena.Code('func_12_420D')
def func_12_420D():
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 21)
    OP_8C(0x0008, 90, 400)
    OP_8E(0x0008, 6450, 0, 2130, 1500, 0x00)

    Return()

# id: 0x0013 offset: 0x4233
@scena.Code('func_13_4233')
def func_13_4233():
    @scena.Lambda('lambda_4239')
    def lambda_4239():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_4239')

    DispatchAsync2(0x00FE, 0x0002, lambda_4239)

    Sleep(500)

    OP_99(0x00FE, 0x03, 0x00, 0x000003E8)
    Sleep(500)

    TerminateThread(0x00FE, 0x02)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 65535)
    ChrTurnDirection(0x00FE, 0x000F, 400)

    Return()

# id: 0x0014 offset: 0x4279
@scena.Code('func_14_4279')
def func_14_4279():
    OP_8E(0x00FE, 1780, 0, 1520, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0015 offset: 0x4295
@scena.Code('func_15_4295')
def func_15_4295():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_42AA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('func_15_4295')

    def _loc_42AA(): pass

    label('loc_42AA')

    Return()

# id: 0x0016 offset: 0x42AB
@scena.Code('func_16_42AB')
def func_16_42AB():
    Sleep(500)

    OP_22(0x008C, 0x00, 0x64)
    OP_8E(0x000E, 1010, 1500, 2110, 5000, 0x00)
    SetChrSubChip(0x000E, 0)
    SetChrChipByIndex(0x000E, 39)
    CreateThread(0x000E, 0x00, 0x00, 0x0015)
    OP_8C(0x000E, 90, 400)
    OP_8F(0x000E, 1830, 100, 1530, 2000, 0x00)

    Return()

# id: 0x0017 offset: 0x42F6
@scena.Code('func_17_42F6')
def func_17_42F6():
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_4304')
    def lambda_4304():
        OP_6D(390, 0, 2650, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4304)

    @scena.Lambda('lambda_431C')
    def lambda_431C():
        OP_6B(500, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_431C)

    Sleep(200)

    SetChrChipByIndex(0x0008, 32)
    SetChrSubChip(0x0008, 2)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_4340')
    def lambda_4340():
        OP_96(0x0008, 0x00000CEE, 0x00000000, 0x0000073A, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4340)

    Sleep(200)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    Fade(250)
    OP_6D(640, 0, 1950, 0)
    OP_67(0, 8980, -10000, 0)
    OP_6C(315000, 0)
    OP_6B(800, 0)
    OP_6E(872, 0)
    WaitForThreadExit(0x0008, 0x0002)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 24)
    SetChrSubChip(0x0008, 6)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010231039V#1004F#5P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x06, 0x08, 0x000007D0)
    OP_22(0x01FB, 0x00, 0x64)
    OP_99(0x0008, 0x09, 0x0C, 0x00001388)
    OP_22(0x0245, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7C(0x00000064, 0x00000000, 0x00001388, 0x000003E8)

    @scena.Lambda('lambda_4425')
    def lambda_4425():
        OP_6B(900, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4425)

    PlayEffect(0x02, 0xFF, 0x00FF, 1690, 0, 1790, 0, 90, 90, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x02, 0x0008, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0101, 0x03, 0x00, 0x0019)
    Sleep(100)

    CreateThread(0x00F7, 0x03, 0x00, 0x001A)
    Sleep(100)

    CreateThread(0x00F9, 0x03, 0x00, 0x001B)
    Sleep(100)

    CreateThread(0x0107, 0x03, 0x00, 0x001C)
    OP_82(0x03, 0x00)

    Return()

# id: 0x0018 offset: 0x44C8
@scena.Code('func_18_44C8')
def func_18_44C8():
    ClearMapFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_44DC')
    def lambda_44DC():
        OP_6D(1640, 0, 2600, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44DC)

    @scena.Lambda('lambda_44F4')
    def lambda_44F4():
        OP_67(0, 6980, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_44F4)

    @scena.Lambda('lambda_450C')
    def lambda_450C():
        OP_6B(820, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_450C)

    @scena.Lambda('lambda_451C')
    def lambda_451C():
        OP_6C(330000, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_451C)

    @scena.Lambda('lambda_452C')
    def lambda_452C():
        OP_6E(872, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_452C)

    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0008, 0x0004)
    Sleep(200)

    OP_7D(0x00, 0x0008, 0x001E, 0x00C8)
    SetChrChipByIndex(0x0008, 32)
    SetChrSubChip(0x0008, 2)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_4562')
    def lambda_4562():
        OP_96(0x0008, 0x00001090, 0xFFFFFF38, 0x00000780, 0x000002BC, 0x00001388)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4562)

    Sleep(200)

    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    WaitForThreadExit(0x0008, 0x0002)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 30)
    SetChrSubChip(0x0008, 27)
    ClearChrFlags(0x0008, 0x0100)
    OP_D1(8, 24000, -30000, 0, 0)
    SetChrPos(0x0008, 3540, 0, 2120, 270)

    ExecExpressionWithValue(
        0x0008,
        0x2D,
        (
            (Expr.PushLong, 0x280),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2E,
        (
            (Expr.PushLong, 0x280),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2F,
        (
            (Expr.PushLong, 0x280),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x04, 0x01, 0x0008, 300, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0x02, 0x0008, 400, 750, -100, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010231040V#1004F#6P#10A咦……！？',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x00)
    OP_83(0x01, 0x02)

    @scena.Lambda('lambda_468C')
    def lambda_468C():
        OP_99(0x00FE, 0x1B, 0x1E, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_468C)

    OP_82(0x01, 0x00)
    OP_82(0x02, 0x00)
    Sleep(200)

    OP_22(0x0245, 0x00, 0x64)

    @scena.Lambda('lambda_46AC')
    def lambda_46AC():
        OP_6D(1080, 0, 1580, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_46AC)

    @scena.Lambda('lambda_46C4')
    def lambda_46C4():
        OP_67(0, 7980, -10000, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_46C4)

    @scena.Lambda('lambda_46DC')
    def lambda_46DC():
        OP_6C(315000, 300)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_46DC)

    @scena.Lambda('lambda_46EC')
    def lambda_46EC():
        OP_D1(254, 34000, -45000, 0, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_46EC)

    OP_7C(0x000000C8, 0x00000000, 0x00001388, 0x000003E8)
    PlayEffect(0x02, 0xFF, 0x00FF, 1980, 0, 1580, 0, 0, 60, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x03, 0x0008, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0101, 0x03, 0x00, 0x0019)
    Sleep(100)

    OP_82(0x03, 0x02)
    CreateThread(0x00F7, 0x03, 0x00, 0x001A)
    Sleep(100)

    CreateThread(0x00F9, 0x03, 0x00, 0x001B)
    Sleep(100)

    CreateThread(0x0107, 0x03, 0x00, 0x001C)

    Return()

# id: 0x0019 offset: 0x47AA
@scena.Code('func_19_47AA')
def func_19_47AA():
    SetChrPos(0x0012, 2590, 0, 640, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 1)
    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x01, 0x00, 0x0101, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_4805')
    def lambda_4805():
        OP_8F(0x00FE, 1790, 0, 60, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4805)

    @scena.Lambda('lambda_4820')
    def lambda_4820():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_4820)

    Sleep(500)

    OP_82(0x01, 0x02)

    ChrTalk(
        0x0012,
        (
            '#1021F#10A#4P唔！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Return()

# id: 0x001A offset: 0x4856
@scena.Code('func_1A_4856')
def func_1A_4856():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_48F9',
    )

    SetChrSubChip(0x0106, 0)
    SetChrChipByIndex(0x0106, 10)
    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0106, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_48A7')
    def lambda_48A7():
        OP_8F(0x00FE, 520, -20, 2680, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_48A7)

    @scena.Lambda('lambda_48C2')
    def lambda_48C2():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_48C2)

    Sleep(500)

    OP_82(0x01, 0x02)

    ChrTalk(
        0x0106,
        (
            '#056F#10A#2P啊！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Jump('loc_4992')

    def _loc_48F9(): pass

    label('loc_48F9')

    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0103, 10)
    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0103, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_4943')
    def lambda_4943():
        OP_8F(0x00FE, 520, -20, 2680, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4943)

    @scena.Lambda('lambda_495E')
    def lambda_495E():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_495E)

    Sleep(500)

    OP_82(0x01, 0x02)

    ChrTalk(
        0x0103,
        (
            '#523F#10A#2P唔！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    def _loc_4992(): pass

    label('loc_4992')

    Return()

# id: 0x001B offset: 0x4993
@scena.Code('func_1B_4993')
def func_1B_4993():
    OP_22(0x01FB, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A43',
    )

    SetChrSubChip(0x0104, 0)
    SetChrChipByIndex(0x0104, 13)
    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x01, 0x02, 0x0104, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_49EF')
    def lambda_49EF():
        OP_8F(0x00FE, -1040, -10, 1760, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_49EF)

    @scena.Lambda('lambda_4A0A')
    def lambda_4A0A():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_4A0A)

    Sleep(500)

    OP_82(0x01, 0x02)

    ChrTalk(
        0x0104,
        (
            '#039F#10A#1P呜哦！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Jump('loc_4ADC')

    def _loc_4A43(): pass

    label('loc_4A43')

    SetChrSubChip(0x0105, 0)
    SetChrChipByIndex(0x0105, 16)
    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x01, 0x02, 0x0105, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_4A8D')
    def lambda_4A8D():
        OP_8F(0x00FE, -1040, -10, 1760, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4A8D)

    @scena.Lambda('lambda_4AA8')
    def lambda_4AA8():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_4AA8)

    Sleep(500)

    OP_82(0x01, 0x00)

    ChrTalk(
        0x0105,
        (
            '#541F#10A#1P呀！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    def _loc_4ADC(): pass

    label('loc_4ADC')

    Return()

# id: 0x001C offset: 0x4ADD
@scena.Code('func_1C_4ADD')
def func_1C_4ADD():
    SetChrSubChip(0x0107, 0)
    SetChrChipByIndex(0x0107, 4)
    OP_22(0x0209, 0x00, 0x64)

    @scena.Lambda('lambda_4AF2')
    def lambda_4AF2():
        OP_8F(0x00FE, 60, 0, -420, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4AF2)

    @scena.Lambda('lambda_4B0D')
    def lambda_4B0D():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_4B0D)

    Sleep(500)

    OP_82(0x01, 0x02)

    ChrTalk(
        0x0107,
        (
            '#0070231044V#068F#10A#3P哇呜！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Return()

# id: 0x001D offset: 0x4B50
@scena.Code('func_1D_4B50')
def func_1D_4B50():
    SetChrFlags(0x0008, 0x0020)
    OP_7C(0x00000064, 0x00000000, 0x00001388, 0x000003E8)

    @scena.Lambda('lambda_4B6C')
    def lambda_4B6C():
        OP_8F(0x00FE, 6520, 0, 900, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4B6C)

    OP_99(0x000F, 0x04, 0x07, 0x000005DC)
    OP_99(0x000F, 0x04, 0x07, 0x000005DC)
    OP_A2(0x0000)

    @scena.Lambda('lambda_4B9C')
    def lambda_4B9C():
        OP_99(0x000F, 0x08, 0x0E, 0x000007D0)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4B9C)

    WaitForThreadExit(0x000F, 0x0001)
    Sleep(400)

    Return()

# id: 0x001E offset: 0x4BB1
@scena.Code('func_1E_4BB1')
def func_1E_4BB1():
    SetChrChipByIndex(0x0008, 37)
    SetChrSubChip(0x0008, 2)
    Sleep(200)

    CreateThread(0x0008, 0x03, 0x00, 0x001F)
    def _loc_4BC7(): pass

    label('loc_4BC7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4BF0',
    )

    OP_9E(0x0008, 0x00000096, 0x00000000, 0x000001F4, 0x00000FA0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4BED',
    )

    Jump('loc_4BF0')

    def _loc_4BED(): pass

    label('loc_4BED')

    Jump('loc_4BC7')

    def _loc_4BF0(): pass

    label('loc_4BF0')

    Sleep(400)

    PlayEffect(0x07, 0xFF, 0x0008, 500, 500, 1000, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_4C30')
    def lambda_4C30():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4C30)

    OP_7C(0x00000064, 0x00000000, 0x00001388, 0x000003E8)
    OP_22(0x022A, 0x00, 0x64)

    @scena.Lambda('lambda_4C60')
    def lambda_4C60():
        OP_96(0x0008, 0x00001BD0, 0x00000000, 0x0000028A, 0x000000C8, 0x00001770)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_4C60)

    WaitForThreadExit(0x0008, 0x0003)
    WaitForThreadExit(0x0008, 0x0002)
    Fade(100)
    SetChrChipByIndex(0x0008, 31)
    SetChrSubChip(0x0008, 0)

    Return()

# id: 0x001F offset: 0x4C92
@scena.Code('func_1F_4C92')
def func_1F_4C92():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4CE2',
    )

    PlayEffect(0x06, 0xFF, 0x0008, 500, 500, 1000, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4CDF',
    )

    Jump('loc_4CE2')

    def _loc_4CDF(): pass

    label('loc_4CDF')

    Jump('func_1F_4C92')

    def _loc_4CE2(): pass

    label('loc_4CE2')

    Return()

# id: 0x0020 offset: 0x4CE3
@scena.Code('func_20_4CE3')
def func_20_4CE3():
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
        (0x00000000, 'loc_4D5D'),
        (0x00000001, 'loc_4D63'),
        (-1, 'loc_4D69'),
    )

    def _loc_4D5D(): pass

    label('loc_4D5D')

    OP_A2(0x1200)

    Jump('loc_4D69')

    def _loc_4D63(): pass

    label('loc_4D63')

    OP_A2(0x1201)

    Jump('loc_4D69')

    def _loc_4D69(): pass

    label('loc_4D69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4D77',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4D7B')

    def _loc_4D77(): pass

    label('loc_4D77')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4D7B(): pass

    label('loc_4D7B')

    Return()

# id: 0x0021 offset: 0x4D7C
@scena.Code('func_21_4D7C')
def func_21_4D7C():
    ClearMapFlags(0x00000001)
    OP_6D(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4DB6',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x0006,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0xFFFF,
        ),
    )

    Jump('loc_4DD0')

    def _loc_4DB6(): pass

    label('loc_4DB6')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x0006,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0xFFFF,
        ),
    )

    def _loc_4DD0(): pass

    label('loc_4DD0')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0022 offset: 0x4DE2
@scena.Code('func_22_4DE2')
def func_22_4DE2():
    TalkBegin(0x00FF)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '有七耀脉的活性化装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【打开开关】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E84',
    )

    Sleep(500)

    OP_22(0x009C, 0x00, 0x64)
    Sleep(1000)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '什么也没有发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4E91')

    def _loc_4E84(): pass

    label('loc_4E84')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E91',
    )

    def _loc_4E91(): pass

    label('loc_4E91')

    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
