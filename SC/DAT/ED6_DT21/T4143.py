import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4143_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4143   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '戴尔蒙'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4143.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1417
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
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -270,
            z                   = 0,
            y                   = 2120,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -440,
            triggerZ            = 0,
            triggerY            = 680,
            triggerRange        = 400,
            actorX              = -270,
            actorZ              = 1500,
            actorY              = 2120,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 6, 0x20EE)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_119',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    def _loc_119(): pass

    label('loc_119')

    Return()

# id: 0x0001 offset: 0x11A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x11B
@scena.Code('ReInit')
def ReInit():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x120
@scena.Code('func_03_120')
def func_03_120():
    TalkBegin(0x0008)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_218',
    )

    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0490371091V#660F有钱能使鬼推磨……\n',
            '欢迎来到戴尔蒙商会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371092V呵呵……想要耀晶片的话，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371093V不过，该给的钱\n',
            '还是要给的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FB')

    def _loc_218(): pass

    label('loc_218')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E1',
    )

    def _loc_225(): pass

    label('loc_225')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x63),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D2',
    )

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
        -1,
        65,
        1,
        (
            TXT(0x00, '地之耀晶片　１００个　３０００米拉\n'),
            TXT(0x01, '水之耀晶片　１００个　３０００米拉\n'),
            TXT(0x02, '火之耀晶片　１００个　３０００米拉\n'),
            TXT(0x03, '风之耀晶片　１００个　３０００米拉\n'),
            TXT(0x04, '时之耀晶片　１００个　３０００米拉\n'),
            TXT(0x05, '空之耀晶片　１００个　９０００米拉\n'),
            TXT(0x06, '幻之耀晶片　１００个　６０００米拉\n'),
            TXT(0x07, '退出\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_384'),
        (0x00000001, 'loc_3D6'),
        (0x00000002, 'loc_428'),
        (0x00000003, 'loc_47A'),
        (0x00000004, 'loc_4CC'),
        (0x00000005, 'loc_51E'),
        (0x00000006, 'loc_570'),
        (-1, 'loc_5C2'),
    )

    def _loc_384(): pass

    label('loc_384')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0xBB8),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3A2',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钱不够了。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3D0')

    def _loc_3A2(): pass

    label('loc_3A2')

    SubMira(3000)
    AddSepith(0x00, 0x0064)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#56I 得到１００个地之耀晶片。',
            TxtCtl.Enter,
        ),
    )

    def _loc_3D0(): pass

    label('loc_3D0')

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5CF')

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0xBB8),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3F4',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钱不够了。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_422')

    def _loc_3F4(): pass

    label('loc_3F4')

    SubMira(3000)
    AddSepith(0x01, 0x0064)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#57I 得到１００个水之耀晶片。',
            TxtCtl.Enter,
        ),
    )

    def _loc_422(): pass

    label('loc_422')

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5CF')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0xBB8),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_446',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钱不够了。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_474')

    def _loc_446(): pass

    label('loc_446')

    SubMira(3000)
    AddSepith(0x02, 0x0064)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#58I 得到１００个火之耀晶片。',
            TxtCtl.Enter,
        ),
    )

    def _loc_474(): pass

    label('loc_474')

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5CF')

    def _loc_47A(): pass

    label('loc_47A')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0xBB8),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_498',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钱不够了。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_4C6')

    def _loc_498(): pass

    label('loc_498')

    SubMira(3000)
    AddSepith(0x03, 0x0064)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#59I 得到１００个风之耀晶片。',
            TxtCtl.Enter,
        ),
    )

    def _loc_4C6(): pass

    label('loc_4C6')

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5CF')

    def _loc_4CC(): pass

    label('loc_4CC')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0xBB8),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4EA',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钱不够了。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_518')

    def _loc_4EA(): pass

    label('loc_4EA')

    SubMira(3000)
    AddSepith(0x04, 0x0064)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#62I 得到１００个时之耀晶片。',
            TxtCtl.Enter,
        ),
    )

    def _loc_518(): pass

    label('loc_518')

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5CF')

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x2328),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_53C',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钱不够了。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_56A')

    def _loc_53C(): pass

    label('loc_53C')

    SubMira(9000)
    AddSepith(0x05, 0x0064)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#60I 得到１００个空之耀晶片。',
            TxtCtl.Enter,
        ),
    )

    def _loc_56A(): pass

    label('loc_56A')

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5CF')

    def _loc_570(): pass

    label('loc_570')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x1770),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_58E',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钱不够了。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5BC')

    def _loc_58E(): pass

    label('loc_58E')

    SubMira(6000)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#61I 得到１００个幻之耀晶片。',
            TxtCtl.Enter,
        ),
    )

    def _loc_5BC(): pass

    label('loc_5BC')

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5CF')

    def _loc_5C2(): pass

    label('loc_5C2')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x63),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5CF')

    def _loc_5CF(): pass

    label('loc_5CF')

    Jump('loc_225')

    def _loc_5D2(): pass

    label('loc_5D2')

    FadeIn(300, 0)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_5E1(): pass

    label('loc_5E1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5FB',
    )

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

    def _loc_5FB(): pass

    label('loc_5FB')

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x608
@scena.Code('func_04_608')
def func_04_608():
    EventBegin(0x00)
    OP_6D(1170, -250, -1690, 0)
    OP_67(0, 5380, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -570, -250, -2430, 0)
    SetChrPos(0x0102, 470, -250, -2600, 0)
    SetChrPos(0x00F8, -570, -250, -3710, 0)
    SetChrPos(0x00F9, 520, -250, -3790, 0)
    OP_4A(0x0008, 255)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BE',
    )

    SetChrPos(0x00F9, -570, -250, -3710, 0)
    SetChrPos(0x00F8, 520, -250, -3790, 0)

    def _loc_6BE(): pass

    label('loc_6BE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6ED',
    )

    SetChrPos(0x00F9, -570, -250, -3710, 0)
    SetChrPos(0x00F8, 520, -250, -3790, 0)

    def _loc_6ED(): pass

    label('loc_6ED')

    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010371035V#1015F#6P咦，这种地方\n',
            '居然有店？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '店员',
        (
            '#0490371036V欢迎光临……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0008, 0, 600)
    Sleep(500)

    @scena.Lambda('lambda_077F')
    def lambda_077F():
        OP_8E(0x00FE, -940, 0, 240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_077F)

    Sleep(50)

    @scena.Lambda('lambda_079F')
    def lambda_079F():
        OP_8E(0x00FE, 220, 0, 250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_079F)

    Sleep(80)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_809',
    )

    @scena.Lambda('lambda_07CC')
    def lambda_07CC():
        OP_8E(0x00FE, -960, 0, -1120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_07CC)

    Sleep(70)

    @scena.Lambda('lambda_07EC')
    def lambda_07EC():
        OP_8E(0x00FE, 250, 0, -1080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_07EC)

    Sleep(50)

    Jump('loc_899')

    def _loc_809(): pass

    label('loc_809')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_859',
    )

    @scena.Lambda('lambda_081C')
    def lambda_081C():
        OP_8E(0x00FE, -960, 0, -1120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_081C)

    Sleep(70)

    @scena.Lambda('lambda_083C')
    def lambda_083C():
        OP_8E(0x00FE, 250, 0, -1080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_083C)

    Sleep(50)

    Jump('loc_899')

    def _loc_859(): pass

    label('loc_859')

    @scena.Lambda('lambda_085F')
    def lambda_085F():
        OP_8E(0x00FE, -960, 0, -1120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_085F)

    Sleep(70)

    @scena.Lambda('lambda_087F')
    def lambda_087F():
        OP_8E(0x00FE, 250, 0, -1080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_087F)

    Sleep(50)

    def _loc_899(): pass

    label('loc_899')

    @scena.Lambda('lambda_089F')
    def lambda_089F():
        OP_6D(530, 0, 1970, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_089F)

    @scena.Lambda('lambda_08B7')
    def lambda_08B7():
        OP_67(0, 4900, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_08B7)

    @scena.Lambda('lambda_08CF')
    def lambda_08CF():
        OP_6B(2830, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_08CF)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0102, 0x0003)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010371037V#1000F#6P售货员，这里是什么店？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    NpcTalk(
        0x0008,
        '店员',
        (
            '#0490371038V#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371039V#1000F请问────',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371040V#1042F……没想到会在\n',
            '这种地方碰到你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010371041V#1004F咦，是约修亚的熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020371042V#1043F#2P艾丝蒂尔，这个人\n',
            '你也认识的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371043V#1005F咦咦！？\n',
            '难不成，是结社的家伙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371044V#1035F#2P不，有点不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371045V#1042F希望你能解释清楚呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_8C(0x0101, 0, 400)
    OP_8C(0x0102, 0, 400)
    OP_21()

    ChrTalk(
        0x0102,
        (
            '#0020371046V#1042F原卢安市长……戴尔蒙先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371047V#1004F你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '店员',
        (
            '#0490371048V#5P没办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1D(0x57)
    OP_8C(0x0008, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010371049V#1005F为、为什么你会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371050V#1042F记得你应该是被\n',
            '监禁在雷斯顿要塞的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371051V#666F#5P哼，确实如此，但你可别误会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371052V#664F我会在这里\n',
            '是经过正式手续的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371053V#1009F正式的手续？\n',
            '再没有比这更可疑的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371054V#666F#5P真、真失礼啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371055V#1005F有卢安的事在先，\n',
            '怎么可能相信你！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010371056V竟然让孤儿院里\n',
            '无辜的孩子们遭到那种事！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371057V#663F#5P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020371058V#1035F艾丝蒂尔……先\n',
            '听听他怎么说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371059V#1042F能不能相信\n',
            '之后再判断就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371060V#1009F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0490371061V#666F#5P那、那个事件里\n',
            '我也是受害者啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371062V因为是在记忆混乱的时候，\n',
            '被什么人操纵的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371063V而且，我用留下的财产\n',
            '支付了巨额的保释金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371064V#1044F原来如此，是这么回事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010371065V#1015F保释金是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371066V#1035F#2P还没正式定罪的时候，\n',
            '只要支付一定的钱\n',
            '就能被释放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371067V#1004F什么……做了那么多坏事，\n',
            '只要有钱就会被饶恕？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020371068V#1042F#2P不是被饶恕啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371069V在利贝尔，确定真正犯人之前\n',
            '不将其作为罪犯来对待是原则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371070V作为定罪之前的担保\n',
            '支付相应的米拉\n',
            '就能保证人身自由。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371071V#1035F当然，其间如果逃跑\n',
            '或者藏起来都是不能饶恕的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371072V#664F#5P哼、哼，就是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371073V#1019F嗯～还是\n',
            '有点不能接受……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371074V#1042F#2P不过，戴尔蒙氏会在这里\n',
            '也不奇怪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371075V有可以酌情的余地\n',
            '也不是不能理解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)
    OP_8C(0x0102, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010371076V#1015F呼～不过……\n',
            '你到底在这里干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371077V#662F#5P如你所见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371078V为了复兴戴尔蒙家族，\n',
            '我决定重振旗鼓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371079V首先要在这里做买卖，\n',
            '积蓄复兴所需的资金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371080V#1019F买、买卖啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010371081V#1015F对了对了，\n',
            '这里到底是什么店？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371082V#664F#5P耀晶片店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371083V#1004F耀晶片！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371084V#662F#5P对啊，买卖耀晶片的店\n',
            '在利贝尔的任何地区都没有吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371085V这个着眼点不坏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371086V#1044F确实………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371087V#1042F不过，要购入足够\n',
            '用于交易的大量耀晶片\n',
            '不是相当辛苦吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490371088V#663F#5P这、这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490371089V#664F我有专门的\n',
            '秘密进货途径嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371090V#1019F总……觉得，还是\n',
            '很可疑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()
    OP_1D(0x1A)
    OP_A2(0x20EE)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
