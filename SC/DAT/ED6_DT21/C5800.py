import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5800_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5800   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '居住区域『克雷德尔』外部２'),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5800.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x10AF
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
        ('ED6_DT29/CH12060._CH', 'ED6_DT29/CH12060P._CP'),
        ('ED6_DT29/CH12061._CH', 'ED6_DT29/CH12061P._CP'),
        ('ED6_DT29/CH12190._CH', 'ED6_DT29/CH12190P._CP'),
        ('ED6_DT29/CH12191._CH', 'ED6_DT29/CH12191P._CP'),
        ('ED6_DT29/CH12970._CH', 'ED6_DT29/CH12970P._CP'),
        ('ED6_DT29/CH12971._CH', 'ED6_DT29/CH12971P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -115090,
            z                   = 0,
            y                   = -63840,
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

# id: 0x10003 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -205120,
            z           = -8000,
            y           = -101640,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -180970,
            z           = -8000,
            y           = -82860,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -200190,
            z           = -8000,
            y           = -62040,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -147140,
            z           = 0,
            y           = -92600,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -138240,
            z           = 0,
            y           = -63500,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -167890,
            z           = 0,
            y           = -42410,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x050C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -159230,
            triggerZ            = 0,
            triggerY            = -95940,
            triggerRange        = 1000,
            actorX              = -158560,
            actorZ              = 0,
            actorY              = -95940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -161810,
            triggerZ            = 0,
            triggerY            = -33530,
            triggerRange        = 1000,
            actorX              = -161810,
            actorZ              = 0,
            actorY              = -34220,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1EA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_200',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    Jump('loc_221')

    def _loc_200(): pass

    label('loc_200')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_20C'),
        (-1, 'loc_221'),
    )

    def _loc_20C(): pass

    label('loc_20C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 5, 0x220D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_221',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0005)

    def _loc_221(): pass

    label('loc_221')

    Return()

# id: 0x0001 offset: 0x222
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFB4CE0, 0xFFFCEED8, 0x00230077)
    OP_22(0x01C7, 0x00, 0x64)
    OP_71(0x0007, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 3, 0x230B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_250',
    )

    OP_6F(0x0005, 0)

    Jump('loc_257')

    def _loc_250(): pass

    label('loc_250')

    OP_6F(0x0005, 60)

    def _loc_257(): pass

    label('loc_257')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 4, 0x230C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_269',
    )

    OP_6F(0x0006, 0)

    Jump('loc_270')

    def _loc_269(): pass

    label('loc_269')

    OP_6F(0x0006, 60)

    def _loc_270(): pass

    label('loc_270')

    Return()

# id: 0x0002 offset: 0x271
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xB2, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 3, 0x230B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_2E5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x230B)

    Jump('loc_34B')

    def _loc_2E5(): pass

    label('loc_2E5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_34B(): pass

    label('loc_34B')

    Jump('loc_37F')

    def _loc_34E(): pass

    label('loc_34E')

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
    def _loc_37F(): pass

    label('loc_37F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x38D
@scena.Code('func_03_38D')
def func_03_38D():
    UnlockAchievement(0x02, 0xB3, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 4, 0x230C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_445',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000001E)
    OP_73(0x0006)
    OP_6F(0x0006, 30)
    AddSepith(0x01, 0x0064)
    AddSepith(0x03, 0x0064)
    AddSepith(0x05, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x230C)

    Jump('loc_45F')

    def _loc_445(): pass

    label('loc_445')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_45F(): pass

    label('loc_45F')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x471
@scena.Code('func_04_471')
def func_04_471():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-179400, -7920, -81170, 0)
    OP_67(0, 6920, -10000, 0)
    OP_6B(12360, 0)
    OP_6C(322000, 0)
    OP_6E(451, 0)
    FadeIn(500, 0)
    OP_0D()
    Sleep(2000)

    OP_22(0x007C, 0x00, 0x64)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5700._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x4E5
@scena.Code('func_05_4E5')
def func_05_4E5():
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
        'loc_4FC',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)

    def _loc_4FC(): pass

    label('loc_4FC')

    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    OP_6D(-153000, -8000, -103040, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3770, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x0000001E)
    OP_73(0x0004)

    @scena.Lambda('lambda_058C')
    def lambda_058C():
        OP_6D(-151420, -8000, -108390, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_058C)

    CreateThread(0x0101, 0x01, 0x00, 0x0006)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, 0x0007)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, 0x0008)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, 0x0009)
    Sleep(1500)

    OP_6F(0x0004, 30)
    OP_70(0x0004, 0x00000000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010391156V#1025F#5P呼～终于到了外面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020391157V#1044F#2P……这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_11(0xED, 0xFF, 0xEE, 0x0000C350, 0x000C3500, 0x00000000)
    OP_6D(-214540, -8000, -101210, 0)
    OP_67(0, 3870, -10000, 0)
    OP_6B(11840, 0)
    OP_6C(319000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0699')
    def lambda_0699():
        OP_6D(-158900, -4000, -56630, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0699)

    @scena.Lambda('lambda_06B1')
    def lambda_06B1():
        OP_67(0, 6100, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06B1)

    OP_C8(0x0080, 0x0046, 'C_PLAC26._CH', 0x01, 0x05DC)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    Fade(500)
    OP_11(0xED, 0xFF, 0xEE, 0x0000D6D8, 0x000186A0, 0x00000000)
    OP_6D(-151930, -8000, -108070, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0x0101, 270, 0)
    OP_8C(0x0102, 270, 0)
    OP_8C(0x00F8, 270, 0)
    OP_8C(0x00F9, 270, 0)
    OP_6F(0x0004, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391158V#035F#6P呼……\n',
            '多么美丽的街道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040391159V#030F看来是古代人\n',
            '生活的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D1')

    def _loc_7CF(): pass

    label('loc_7CF')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_834',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391160V#1382F#6P好漂亮的街道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060391161V看来是古代人\n',
            '生活的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D1')

    def _loc_834(): pass

    label('loc_834')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391162V#020F#6P……好漂亮的街道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030391163V应该是古代人\n',
            '生活的地方吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D1')

    def _loc_89A(): pass

    label('loc_89A')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8FF',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391164V#1060F#6P好漂亮的街道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180391165V应该是古代人\n',
            '生活的地方吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D1')

    def _loc_8FF(): pass

    label('loc_8FF')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_967',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391166V#070F#6P嗯，好漂亮的街道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080391167V看来是古代人\n',
            '生活的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D1')

    def _loc_967(): pass

    label('loc_967')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D1',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391168V#064F#6P哇～好漂亮的街道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070391169V#061F看来是古代人\n',
            '生活的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9D1(): pass

    label('loc_9D1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A31',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391170V#051F#6P的确，和我们迫降的地方相比，\n',
            '更有着人们生活过的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1A')

    def _loc_A31(): pass

    label('loc_A31')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A93',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391171V#560F#6P的确，和我们迫降的地方相比，\n',
            '更有着人们生活过的气息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1A')

    def _loc_A93(): pass

    label('loc_A93')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391172V#070F#6P的确，和我们迫降的地方相比，\n',
            '更有着人们生活过的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1A')

    def _loc_AF3(): pass

    label('loc_AF3')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B58',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391173V#1060F#6P的确，和我们迫降的地方相比，\n',
            '好像更有着人们生活过的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1A')

    def _loc_B58(): pass

    label('loc_B58')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BBA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391174V#027F#6P的确，和我们迫降的地方相比，\n',
            '更有着人们生活过的气息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1A')

    def _loc_BBA(): pass

    label('loc_BBA')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C1A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391175V#1382F#6P的确，和我们迫降的地方相比，\n',
            '更有着人们生活过的气息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C1A(): pass

    label('loc_C1A')

    ChrTalk(
        0x0101,
        (
            '#0010391176V#1006F#6P嗯……\n',
            '这里的气氛似乎非常安静祥和。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391177V#1015F但是……为什么过去的人们\n',
            '要放弃这么美好的都市呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391178V#1035F#6P……调查一下的话，\n',
            '说不定可以了解到当时的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391179V#1040F反正也要寻找新的路线，\n',
            '就赶快探索一下这附近吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D30')
    def lambda_0D30():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D30)

    Sleep(50)

    @scena.Lambda('lambda_0D43')
    def lambda_0D43():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0D43)

    Sleep(50)

    @scena.Lambda('lambda_0D56')
    def lambda_0D56():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0D56)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010391180V#1006F#5P嗯，ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    OP_A2(0x2218)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xDB1
@scena.Code('func_06_DB1')
def func_06_DB1():
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -151160, -7920, -102500, 180)
    OP_8E(0x00FE, -150970, -8000, -105930, 2000, 0x00)
    OP_8E(0x00FE, -151660, -8000, -109740, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0007 offset: 0xDFA
@scena.Code('func_07_DFA')
def func_07_DFA():
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -151160, -7920, -102500, 180)
    OP_8E(0x00FE, -150970, -8000, -105930, 2000, 0x00)
    OP_8E(0x00FE, -149980, -8000, -109770, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0008 offset: 0xE4A
@scena.Code('func_08_E4A')
def func_08_E4A():
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -151160, -7920, -102500, 180)
    OP_8E(0x00FE, -150970, -8000, -105930, 2000, 0x00)
    OP_8E(0x00FE, -151880, -8000, -108190, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0009 offset: 0xE9A
@scena.Code('func_09_E9A')
def func_09_E9A():
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -151160, -7920, -102500, 180)
    OP_8E(0x00FE, -150970, -8000, -105930, 2000, 0x00)
    OP_8E(0x00FE, -150190, -8000, -108160, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000A offset: 0xEEA
@scena.Code('func_0A_EEA')
def func_0A_EEA():
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
        (0x00000000, 'loc_F64'),
        (0x00000001, 'loc_F6A'),
        (-1, 'loc_F70'),
    )

    def _loc_F64(): pass

    label('loc_F64')

    OP_A2(0x1200)

    Jump('loc_F70')

    def _loc_F6A(): pass

    label('loc_F6A')

    OP_A2(0x1201)

    Jump('loc_F70')

    def _loc_F70(): pass

    label('loc_F70')

    Return()

# id: 0x000B offset: 0xF71
@scena.Code('func_0B_F71')
def func_0B_F71():
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

# id: 0x000C offset: 0x1002
@scena.Code('func_0C_1002')
def func_0C_1002():
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
