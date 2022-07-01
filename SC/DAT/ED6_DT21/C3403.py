import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3403   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ' '),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3403.x'
    header.mapIndex       = 1
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x100C
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
            x           = -39890,
            z           = 0,
            y           = 38220,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -26760,
            z           = 0,
            y           = 11040,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 2720,
            z           = 0,
            y           = -14290,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x18E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 880,
            y           = 0,
            z           = -49130,
            range       = 10060,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF4B7E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10005 offset: 0x1AE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 10810,
            triggerZ            = 0,
            triggerY            = 31850,
            triggerRange        = 1000,
            actorX              = 11490,
            actorZ              = 0,
            actorY              = 31930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3060,
            triggerZ            = 0,
            triggerY            = -61790,
            triggerRange        = 1000,
            actorX              = -3060,
            actorZ              = 0,
            actorY              = -62430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10970,
            triggerZ            = 0,
            triggerY            = -47730,
            triggerRange        = 1000,
            actorX              = -11680,
            actorZ              = 0,
            actorY              = -47710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x21A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x21B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AD, 0, 0x1568)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_234')

    def _loc_22D(): pass

    label('loc_22D')

    OP_6F(0x0000, 60)

    def _loc_234(): pass

    label('loc_234')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AD, 2, 0x156A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_246',
    )

    OP_6F(0x0001, 0)

    Jump('loc_24D')

    def _loc_246(): pass

    label('loc_246')

    OP_6F(0x0001, 60)

    def _loc_24D(): pass

    label('loc_24D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AD, 3, 0x156B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_266')

    def _loc_25F(): pass

    label('loc_25F')

    OP_6F(0x0002, 60)

    def _loc_266(): pass

    label('loc_266')

    OP_BE(0x00, 0x04, 0x0002, 0x0002, 0x0000, 0x01, -4380, -1120, -52330, 3600, 3000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2AC',
    )

    OP_82(0x87, 0x00)
    OP_82(0x88, 0x00)
    OP_82(0x89, 0x00)
    OP_82(0x8A, 0x00)
    OP_82(0x8B, 0x00)
    OP_82(0x8C, 0x00)
    OP_82(0x91, 0x00)
    OP_22(0x01C7, 0x00, 0x64)

    Jump('loc_2B8')

    def _loc_2AC(): pass

    label('loc_2AC')

    CreateThread(0x0008, 0x00, 0x00, 0x000A)
    OP_22(0x010B, 0x00, 0x64)

    def _loc_2B8(): pass

    label('loc_2B8')

    Return()

# id: 0x0002 offset: 0x2B9
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_2CE(): pass

    label('loc_2CE')

    Return()

# id: 0x0003 offset: 0x2CF
@scena.Code('func_03_2CF')
def func_03_2CF():
    UnlockAchievement(0x02, 0xC4, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AD, 0, 0x1568)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3ED',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000001E)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    AddSepith(0x00, 0x0014)
    AddSepith(0x01, 0x0014)
    AddSepith(0x02, 0x0014)
    AddSepith(0x03, 0x0014)
    AddSepith(0x04, 0x0014)
    AddSepith(0x05, 0x0014)
    AddSepith(0x06, 0x0014)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1568)

    Jump('loc_407')

    def _loc_3ED(): pass

    label('loc_3ED')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_407(): pass

    label('loc_407')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x419
@scena.Code('func_04_419')
def func_04_419():
    UnlockAchievement(0x02, 0xC5, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AD, 2, 0x156A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F6',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['活性之药'], 1)"),
            Expr.Return,
        ),
        'loc_48D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x156A)

    Jump('loc_4F3')

    def _loc_48D(): pass

    label('loc_48D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['活性之药']),
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

    def _loc_4F3(): pass

    label('loc_4F3')

    Jump('loc_527')

    def _loc_4F6(): pass

    label('loc_4F6')

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
    def _loc_527(): pass

    label('loc_527')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x535
@scena.Code('func_05_535')
def func_05_535():
    UnlockAchievement(0x02, 0xC6, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AD, 3, 0x156B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_612',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['导力活火炮'], 1)"),
            Expr.Return,
        ),
        'loc_5A9',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力活火炮']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x156B)

    Jump('loc_60F')

    def _loc_5A9(): pass

    label('loc_5A9')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['导力活火炮']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['导力活火炮']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_60F(): pass

    label('loc_60F')

    Jump('loc_643')

    def _loc_612(): pass

    label('loc_612')

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
    def _loc_643(): pass

    label('loc_643')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x651
@scena.Code('func_06_651')
def func_06_651():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 4, 0x1424)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_65D',
    )

    Return()

    def _loc_65D(): pass

    label('loc_65D')

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
        'loc_67D',
    )

    Call(0, 0x0007)
    Call(0, 0x0008)
    FadeIn(0, 0)

    def _loc_67D(): pass

    label('loc_67D')

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    Sleep(200)

    Fade(1000)
    OP_6D(-1690, -650, -51270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 4880, 0, -47730, 219)
    SetChrPos(0x0107, 6180, 0, -47670, 220)
    SetChrPos(0x00F9, 4620, 0, -46710, 234)
    SetChrPos(0x00F7, 6170, 0, -48910, 240)
    OP_0D()

    @scena.Lambda('lambda_072B')
    def lambda_072B():
        OP_8E(0x00FE, -420, 0, -50740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_072B)

    Sleep(300)

    @scena.Lambda('lambda_074B')
    def lambda_074B():
        OP_8E(0x00FE, 70, 0, -52090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_074B)

    Sleep(500)

    @scena.Lambda('lambda_076B')
    def lambda_076B():
        OP_8E(0x00FE, 570, 0, -51030, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_076B)

    Sleep(400)

    @scena.Lambda('lambda_078B')
    def lambda_078B():
        OP_8E(0x00FE, -180, 0, -49700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_078B)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_07AB')
    def lambda_07AB():
        OP_8C(0x0101, 257, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07AB)

    @scena.Lambda('lambda_07B9')
    def lambda_07B9():
        OP_6D(-755, 0, -50870, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07B9)

    WaitForThreadExit(0x00F7, 0x0001)

    @scena.Lambda('lambda_07D6')
    def lambda_07D6():
        OP_8C(0x00F7, 257, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_07D6)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_07E9')
    def lambda_07E9():
        OP_8C(0x0107, 257, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_07E9)

    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_07FC')
    def lambda_07FC():
        OP_8C(0x00F9, 257, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_07FC)

    WaitForThreadExit(0x0107, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0107,
        (
            '#0070230942V#560F哇……\n',
            '这里没沸腾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230943V#061F嘿嘿，感觉\n',
            '好像很舒服呢。',
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
        'loc_945',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230944V#030F#5P呼，那么\n',
            '我们该做的事情\n',
            '就只有一件了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230945V#031F嘿嘿，坦诚相见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230946V#1007F#2P别擅自脱掉啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230947V#1006F不过也好，看来是不错的温泉，\n',
            '泡泡脚也不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E6')

    def _loc_945(): pass

    label('loc_945')

    ChrTalk(
        0x0105,
        (
            '#0060230948V#542F#5P的确，满身大汗的，\n',
            '让人忍不住就想下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230949V#1016F#2P嗯嗯，我也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230950V#1006F看来是不错的温泉\n',
            '泡泡脚也不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E6(): pass

    label('loc_9E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A21',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230951V#552F……真是的，适可而止一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A52')

    def _loc_A21(): pass

    label('loc_A21')

    ChrTalk(
        0x0103,
        (
            '#0030230952V#021F呵呵，这就是所谓的足浴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A52(): pass

    label('loc_A52')

    OP_A2(0x1424)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xA58
@scena.Code('func_07_A58')
def func_07_A58():
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
        (0x00000000, 'loc_AD2'),
        (0x00000001, 'loc_AD8'),
        (-1, 'loc_ADE'),
    )

    def _loc_AD2(): pass

    label('loc_AD2')

    OP_A2(0x1200)

    Jump('loc_ADE')

    def _loc_AD8(): pass

    label('loc_AD8')

    OP_A2(0x1201)

    Jump('loc_ADE')

    def _loc_ADE(): pass

    label('loc_ADE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_AEC',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_AF0')

    def _loc_AEC(): pass

    label('loc_AEC')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_AF0(): pass

    label('loc_AF0')

    Return()

# id: 0x0008 offset: 0xAF1
@scena.Code('func_08_AF1')
def func_08_AF1():
    ClearMapFlags(0x00000001)
    OP_6D(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B2B',
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

    Jump('loc_B45')

    def _loc_B2B(): pass

    label('loc_B2B')

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

    def _loc_B45(): pass

    label('loc_B45')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0009 offset: 0xB57
@scena.Code('func_09_B57')
def func_09_B57():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '正好有温度适中的温泉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        10,
        10,
        1,
        (
            TXT(0x00, '享受足浴。\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_BD6'),
        (0x00000001, 'loc_D37'),
        (-1, 'loc_D3A'),
    )

    def _loc_BD6(): pass

    label('loc_BD6')

    FadeOut(1000, 0, -1)
    Sleep(600)

    OP_22(0x00A2, 0x00, 0x64)
    Sleep(1500)

    OP_22(0x000B, 0x00, 0x64)
    Sleep(800)

    OP_0D()
    SetChrPos(0x0000, 820, 0, -51320, 90)
    SetChrPos(0x0001, 820, 0, -51320, 90)
    SetChrPos(0x0002, 820, 0, -51320, 90)
    SetChrPos(0x0003, 820, 0, -51320, 90)
    SetChrPos(0x0004, 820, 0, -51320, 90)
    SetChrPos(0x0005, 820, 0, -51320, 90)
    SetChrPos(0x0006, 820, 0, -51320, 90)
    SetChrPos(0x0007, 820, 0, -51320, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C95',
    )

    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFB, 0)

    def _loc_C95(): pass

    label('loc_C95')

    If(
        (
            (Expr.Eval, "OP_42(0x01)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CA8',
    )

    SetChrStatus(ChrTable['约修亚'], 0xFB, 0)

    def _loc_CA8(): pass

    label('loc_CA8')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CBB',
    )

    SetChrStatus(ChrTable['雪拉扎德'], 0xFB, 0)

    def _loc_CBB(): pass

    label('loc_CBB')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CCE',
    )

    SetChrStatus(ChrTable['奥利维尔'], 0xFB, 0)

    def _loc_CCE(): pass

    label('loc_CCE')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE1',
    )

    SetChrStatus(ChrTable['阿加特'], 0xFB, 0)

    def _loc_CE1(): pass

    label('loc_CE1')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CF4',
    )

    SetChrStatus(ChrTable['科洛丝'], 0xFB, 0)

    def _loc_CF4(): pass

    label('loc_CF4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D07',
    )

    SetChrStatus(ChrTable['提妲'], 0xFB, 0)

    def _loc_D07(): pass

    label('loc_D07')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D1A',
    )

    SetChrStatus(ChrTable['金'], 0xFB, 0)

    def _loc_D1A(): pass

    label('loc_D1A')

    OP_8C(0x0000, 90, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x00)
    FadeIn(1000, 0)
    OP_0D()

    Jump('loc_D3D')

    def _loc_D37(): pass

    label('loc_D37')

    Jump('loc_D3D')

    def _loc_D3A(): pass

    label('loc_D3A')

    Jump('loc_D3D')

    def _loc_D3D(): pass

    label('loc_D3D')

    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0xD41
@scena.Code('func_0A_D41')
def func_0A_D41():
    Call(0, 0x000B)
    CreateThread(0x0008, 0x03, 0x00, 0x000C)
    PlayEffect(0x9B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9B, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0x9C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9C, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0x9D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9D, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0x9E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9E, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0x9F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9F, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0xA0, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0xA0, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0xA1, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0xA1, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0xA2, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0xA2, 0x01, 0x0000006E)
    Call(0, 0x000B)
    PlayEffect(0xA3, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0xA3, 0x01, 0x0000006E)

    Return()

# id: 0x000B offset: 0xF89
@scena.Code('func_0B_F89')
def func_0B_F89():
    Switch(
        (
            Expr.Rand,
            (Expr.PushLong, 0x5),
            Expr.Mod,
            Expr.Return,
        ),
        (0x00000000, 'loc_FAA'),
        (0x00000001, 'loc_FB2'),
        (0x00000002, 'loc_FBA'),
        (0x00000003, 'loc_FC2'),
        (0x00000004, 'loc_FCA'),
        (-1, 'loc_FD2'),
    )

    def _loc_FAA(): pass

    label('loc_FAA')

    Sleep(500)

    Jump('loc_FDA')

    def _loc_FB2(): pass

    label('loc_FB2')

    Sleep(1000)

    Jump('loc_FDA')

    def _loc_FBA(): pass

    label('loc_FBA')

    Sleep(1500)

    Jump('loc_FDA')

    def _loc_FC2(): pass

    label('loc_FC2')

    Sleep(2000)

    Jump('loc_FDA')

    def _loc_FCA(): pass

    label('loc_FCA')

    Sleep(2500)

    Jump('loc_FDA')

    def _loc_FD2(): pass

    label('loc_FD2')

    Sleep(3000)

    Jump('loc_FDA')

    def _loc_FDA(): pass

    label('loc_FDA')

    Return()

# id: 0x000C offset: 0xFDB
@scena.Code('func_0C_FDB')
def func_0C_FDB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FF1',
    )

    OP_22(0x010D, 0x00, 0x64)
    Sleep(7000)

    Jump('func_0C_FDB')

    def _loc_FF1(): pass

    label('loc_FF1')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
