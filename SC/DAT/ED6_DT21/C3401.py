import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ' '),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3401.x'
    header.mapIndex       = 1
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xC7B
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
        ('ED6_DT29/CH12110._CH', 'ED6_DT29/CH12110P._CP'),
        ('ED6_DT29/CH12111._CH', 'ED6_DT29/CH12111P._CP'),
        ('ED6_DT29/CH12410._CH', 'ED6_DT29/CH12410P._CP'),
        ('ED6_DT29/CH12411._CH', 'ED6_DT29/CH12411P._CP'),
        ('ED6_DT29/CH12250._CH', 'ED6_DT29/CH12250P._CP'),
        ('ED6_DT29/CH12251._CH', 'ED6_DT29/CH12251P._CP'),
        ('ED6_DT29/CH12130._CH', 'ED6_DT29/CH12130P._CP'),
        ('ED6_DT29/CH12131._CH', 'ED6_DT29/CH12131P._CP'),
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
    ]

# id: 0x10002 offset: 0x11A
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
            npcIndex            = 0x0049,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 860,
            z           = 0,
            y           = -80,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -12680,
            z           = 0,
            y           = -5390,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7430,
            z           = 0,
            y           = 43660,
            word_0C     = 0x00E1,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13610,
            z           = 0,
            y           = -45610,
            word_0C     = 0x010E,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -23680,
            y           = 0,
            z           = 5150,
            range       = -17980,
            dword_10    = 0x000007D0,
            dword_14    = 0x000048A8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10005 offset: 0x1CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 19000,
            triggerZ            = 0,
            triggerY            = 52800,
            triggerRange        = 1000,
            actorX              = 19000,
            actorZ              = 1000,
            actorY              = 52800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12930,
            triggerZ            = 0,
            triggerY            = -51920,
            triggerRange        = 1000,
            actorX              = 13390,
            actorZ              = 0,
            actorY              = -53090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x212
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x213
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 0, 0x1560)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_225',
    )

    OP_6F(0x0000, 0)

    Jump('loc_22C')

    def _loc_225(): pass

    label('loc_225')

    OP_6F(0x0000, 60)

    def _loc_22C(): pass

    label('loc_22C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 1, 0x1561)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23E',
    )

    OP_6F(0x0001, 0)

    Jump('loc_245')

    def _loc_23E(): pass

    label('loc_23E')

    OP_6F(0x0001, 60)

    def _loc_245(): pass

    label('loc_245')

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_384',
    )

    LoadEffect(0x00, 'map\\\\mpsteam0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -12310, -650, 9080, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x00FF, -5900, -650, 7400, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x00FF, -7590, -650, -1210, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x03, 0x00FF, -8800, -650, -3670, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x04, 0x00FF, -12860, -650, -40, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_384(): pass

    label('loc_384')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3A2',
    )

    OP_82(0x80, 0x02)
    OP_82(0x81, 0x02)
    OP_82(0x82, 0x02)
    OP_82(0x83, 0x02)
    OP_82(0x84, 0x02)
    OP_22(0x01C7, 0x00, 0x64)

    Jump('loc_3AE')

    def _loc_3A2(): pass

    label('loc_3A2')

    CreateThread(0x0008, 0x00, 0x00, 0x0007)
    OP_22(0x010B, 0x00, 0x64)

    def _loc_3AE(): pass

    label('loc_3AE')

    Return()

# id: 0x0002 offset: 0x3AF
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xBE, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 0, 0x1560)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_423',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1560)

    Jump('loc_489')

    def _loc_423(): pass

    label('loc_423')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_489(): pass

    label('loc_489')

    Jump('loc_4BD')

    def _loc_48C(): pass

    label('loc_48C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_4BD(): pass

    label('loc_4BD')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x4CB
@scena.Code('func_03_4CB')
def func_03_4CB():
    UnlockAchievement(0x02, 0xBF, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 1, 0x1561)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A8',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_53F',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1561)

    Jump('loc_5A5')

    def _loc_53F(): pass

    label('loc_53F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_5A5(): pass

    label('loc_5A5')

    Jump('loc_5D9')

    def _loc_5A8(): pass

    label('loc_5A8')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_5D9(): pass

    label('loc_5D9')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5E7
@scena.Code('func_04_5E7')
def func_04_5E7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 3, 0x1423)),
            Expr.Return,
        ),
        'loc_5EF',
    )

    Return()

    def _loc_5EF(): pass

    label('loc_5EF')

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
        'loc_60F',
    )

    Call(0, 0x0005)
    Call(0, 0x0006)
    FadeIn(0, 0)

    def _loc_60F(): pass

    label('loc_60F')

    Fade(1000)
    OP_6D(2350, 0, -14430, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(3740, 0)
    OP_6C(150000, 0)
    OP_6E(328, 0)
    CreateThread(0x0008, 0x03, 0x00, 0x0009)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x8D, 0x01, 0x0000006E)
    OP_0D()
    SetChrPos(0x0101, -19860, 0, 6880, 90)
    SetChrPos(0x0107, -21170, 0, 7130, 90)
    SetChrPos(0x00F7, -19760, 0, 8160, 90)
    SetChrPos(0x00F9, -21470, 0, 8690, 90)
    OP_C8(0x0200, 0x0046, 'C_PLAC11._CH', 0x00, 0x03E8)
    ShowPlaceName('温泉源流')
    Sleep(1000)

    @scena.Lambda('lambda_0703')
    def lambda_0703():
        OP_6D(-18400, -30, 6270, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0703)

    @scena.Lambda('lambda_071B')
    def lambda_071B():
        OP_67(0, 5570, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_071B)

    @scena.Lambda('lambda_0733')
    def lambda_0733():
        OP_6B(3840, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0733)

    @scena.Lambda('lambda_0743')
    def lambda_0743():
        OP_6C(138000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0743)

    @scena.Lambda('lambda_0753')
    def lambda_0753():
        OP_6E(262, 6000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_0753)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010230929V#1020F#2P呜哇……\n',
            '沸腾得很厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230930V#065F#4P啊哇哇，要是掉下去\n',
            '一定会被烫伤的……',
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
        'loc_85F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230931V#032F#4P沸腾的热水自不必说……\n',
            '还要留意那些高热的蒸气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230932V一不小心的话\n',
            '可不是烫伤那么简单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DB')

    def _loc_85F(): pass

    label('loc_85F')

    ChrTalk(
        0x0105,
        (
            '#0060230933V#042F#4P沸腾的热水自不必说……\n',
            '高热的蒸气看起来也很危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230934V一不小心的话\n',
            '可不是烫伤那么简单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8DB(): pass

    label('loc_8DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_970',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230935V#053F#6P啊啊……正确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230936V#050F看起来是每隔一定时间\n',
            '就会喷出来的样子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230937V只能算准时机\n',
            '穿越过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9FF')

    def _loc_970(): pass

    label('loc_970')

    ChrTalk(
        0x0103,
        (
            '#0030230938V#026F#6P嗯嗯……说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230939V#022F看起来是每隔一定时间\n',
            '就会喷出来的样子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230940V只能算准时机\n',
            '穿越过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9FF(): pass

    label('loc_9FF')

    ChrTalk(
        0x0101,
        (
            '#0010230941V#1002F#2P嗯，ＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1423)
    OP_28(0x0088, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xA30
@scena.Code('func_05_A30')
def func_05_A30():
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
        (0x00000000, 'loc_AAA'),
        (0x00000001, 'loc_AB0'),
        (-1, 'loc_AB6'),
    )

    def _loc_AAA(): pass

    label('loc_AAA')

    OP_A2(0x1200)

    Jump('loc_AB6')

    def _loc_AB0(): pass

    label('loc_AB0')

    OP_A2(0x1201)

    Jump('loc_AB6')

    def _loc_AB6(): pass

    label('loc_AB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_AC4',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_AC8')

    def _loc_AC4(): pass

    label('loc_AC4')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_AC8(): pass

    label('loc_AC8')

    Return()

# id: 0x0006 offset: 0xAC9
@scena.Code('func_06_AC9')
def func_06_AC9():
    ClearMapFlags(0x00000001)
    OP_6D(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B03',
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

    Jump('loc_B1D')

    def _loc_B03(): pass

    label('loc_B03')

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

    def _loc_B1D(): pass

    label('loc_B1D')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0007 offset: 0xB2F
@scena.Code('func_07_B2F')
def func_07_B2F():
    Call(0, 0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 3, 0x1423)),
            Expr.Return,
        ),
        'loc_B81',
    )

    CreateThread(0x0008, 0x03, 0x00, 0x0009)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x8D, 0x01, 0x0000006E)
    Call(0, 0x0008)

    def _loc_B81(): pass

    label('loc_B81')

    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x8E, 0x01, 0x0000006E)
    Call(0, 0x0008)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x8F, 0x01, 0x0000006E)

    Return()

# id: 0x0008 offset: 0xBFE
@scena.Code('func_08_BFE')
def func_08_BFE():
    Switch(
        (
            Expr.Rand,
            (Expr.PushLong, 0x5),
            Expr.Mod,
            Expr.Return,
        ),
        (0x00000000, 'loc_C1F'),
        (0x00000001, 'loc_C27'),
        (0x00000002, 'loc_C2F'),
        (0x00000003, 'loc_C37'),
        (0x00000004, 'loc_C3F'),
        (-1, 'loc_C47'),
    )

    def _loc_C1F(): pass

    label('loc_C1F')

    Sleep(500)

    Jump('loc_C4F')

    def _loc_C27(): pass

    label('loc_C27')

    Sleep(1000)

    Jump('loc_C4F')

    def _loc_C2F(): pass

    label('loc_C2F')

    Sleep(1500)

    Jump('loc_C4F')

    def _loc_C37(): pass

    label('loc_C37')

    Sleep(2000)

    Jump('loc_C4F')

    def _loc_C3F(): pass

    label('loc_C3F')

    Sleep(2500)

    Jump('loc_C4F')

    def _loc_C47(): pass

    label('loc_C47')

    Sleep(3000)

    Jump('loc_C4F')

    def _loc_C4F(): pass

    label('loc_C4F')

    Return()

# id: 0x0009 offset: 0xC50
@scena.Code('func_09_C50')
def func_09_C50():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C66',
    )

    OP_22(0x010D, 0x00, 0x64)
    Sleep(7000)

    Jump('func_09_C50')

    def _loc_C66(): pass

    label('loc_C66')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
