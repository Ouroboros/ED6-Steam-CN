import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5504_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5504   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亚妮拉丝的头'),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5504.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1C37
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
        ('ED6_DT29/CH12180._CH', 'ED6_DT29/CH12180P._CP'),
        ('ED6_DT29/CH12181._CH', 'ED6_DT29/CH12181P._CP'),
        ('ED6_DT29/CH12230._CH', 'ED6_DT29/CH12230P._CP'),
        ('ED6_DT29/CH12231._CH', 'ED6_DT29/CH12231P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
        ('ED6_DT29/CH12360._CH', 'ED6_DT29/CH12360P._CP'),
        ('ED6_DT29/CH12361._CH', 'ED6_DT29/CH12361P._CP'),
        ('ED6_DT26/CH20268._CH', 'ED6_DT26/CH20268P._CP'),
        ('ED6_DT26/CH20266._CH', 'ED6_DT26/CH20266P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
    ]

# id: 0x10002 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -19520,
            z                   = -200,
            y                   = -19050,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x01F8,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -8610,
            z           = 0,
            y           = 35650,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 890,
            z           = 0,
            y           = 17280,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 24590,
            z           = 0,
            y           = 17330,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0389,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19740,
            z           = 0,
            y           = 29560,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -16170,
            z           = 0,
            y           = 8880,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0389,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1AE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1AE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 24590,
            triggerZ            = 0,
            triggerY            = 35090,
            triggerRange        = 1000,
            actorX              = 25030,
            actorZ              = 0,
            actorY              = 35520,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -28980,
            triggerZ            = 0,
            triggerY            = -18140,
            triggerRange        = 800,
            actorX              = -28980,
            actorZ              = 1000,
            actorY              = -18140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 5, 0x100D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20B',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0004)

    def _loc_20B(): pass

    label('loc_20B')

    Return()

# id: 0x0001 offset: 0x20C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 0, 0x1120)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21E',
    )

    OP_6F(0x0000, 0)

    Jump('loc_225')

    def _loc_21E(): pass

    label('loc_21E')

    OP_6F(0x0000, 60)

    def _loc_225(): pass

    label('loc_225')

    Return()

# id: 0x0002 offset: 0x226
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x8E, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 0, 0x1120)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_303',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['强化皮铠'], 1)"),
            Expr.Return,
        ),
        'loc_29A',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['强化皮铠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1120)

    Jump('loc_300')

    def _loc_29A(): pass

    label('loc_29A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['强化皮铠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['强化皮铠']),
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

    def _loc_300(): pass

    label('loc_300')

    Jump('loc_334')

    def _loc_303(): pass

    label('loc_303')

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
    def _loc_334(): pass

    label('loc_334')

    Sleep(30)

    Call(0, 0x0003)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x346
@scena.Code('func_03_346')
def func_03_346():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 7, 0x100F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_444',
    )

    ChrTalk(
        0x0101,
        (
            '#0010191230V#1004F啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191231V难不成，这个\n',
            '就是我们的装备？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191232V#811F嗯，似乎是呢⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191233V#1310F说不定其它装备\n',
            '也被藏在什么地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191234V#1006F嗯～\n',
            '虽然想避开和魔兽的战斗，\n',
            '但似乎值得探索一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x100F)

    def _loc_444(): pass

    label('loc_444')

    Return()

# id: 0x0004 offset: 0x445
@scena.Code('func_04_445')
def func_04_445():
    EventBegin(0x00)
    OP_20(0x00000BB8)
    FadeOut(0, 0, -1)
    RemoveItem(ItemTable['战斗用棍'], 1)
    RemoveItem(ItemTable['强化皮铠'], 1)
    RemoveItem(ItemTable['强化皮靴'], 1)
    RemoveItem(ItemTable['直刃剑'], 1)
    RemoveItem(ItemTable['强化皮铠'], 1)
    RemoveItem(ItemTable['强化皮靴'], 1)
    OP_6D(-19290, 0, -16309, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -18710, 0, -16030, 268)
    SetChrPos(0x010A, -19980, 0, -19410, 243)
    SetChrFlags(0x0101, 0x0002)
    SetChrFlags(0x010A, 0x0002)
    SetChrChipByIndex(0x0101, 8)
    SetChrChipByIndex(0x010A, 9)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x010A, 0)
    ClearChrFlags(0x0101, 0x0001)
    ClearChrFlags(0x010A, 0x0001)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x10A, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x10A, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x10A, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010191146V#5P#1007F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191147V#1003F……已经早上了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190126V……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191149V#1020F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(1000, 0)
    OP_0D()
    OP_99(0x0101, 0x00, 0x02, 0x000001F4)
    Sleep(500)

    SetChrSubChip(0x0101, 5)
    Sleep(200)

    SetChrSubChip(0x0101, 2)
    Sleep(200)

    SetChrSubChip(0x0101, 5)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010191150V#5P#1020F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191151V这里，是哪里……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191152V记得被敌人袭击之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 5)
    Sleep(100)

    SetChrSubChip(0x0101, 6)
    Sleep(800)

    SetChrSubChip(0x0101, 5)
    Sleep(200)

    SetChrSubChip(0x0101, 7)
    Sleep(500)

    SetChrSubChip(0x0101, 4)
    Sleep(200)

    SetChrSubChip(0x0101, 7)
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0002)
    SetChrFlags(0x0101, 0x0001)
    OP_8C(0x0101, 180, 0)
    OP_0D()
    Sleep(500)

    OP_8E(0x0101, -18570, 0, -18530, 2000, 0x00)
    OP_8C(0x0101, 225, 400)
    Fade(500)
    SetChrChipByIndex(0x0101, 10)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191153V#5P#1002F亚妮拉丝！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191154V快起来，亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191155V#1311F#6P嗯……嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191156V兔子和……\n',
            '熊的娃娃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191157V……要选哪一个呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191158V#5P#1007F在、在做什么梦啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191159V#1005F亚妮拉丝！\n',
            '不得了啦，快起来啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191160V#1316F#6P嗯～……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x010A, 0x00, 0x02, 0x000003E8)
    OP_99(0x010A, 0x02, 0x00, 0x000003E8)
    Sleep(500)

    OP_99(0x010A, 0x00, 0x03, 0x000003E8)

    ChrTalk(
        0x010A,
        (
            '#0120191161V#1314F#6P咦，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191162V啊，对了……\n',
            '已经是晨练的时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191163V#5P#1007F败给你了……\n',
            '现在不是晨练的时候啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191164V#1014F拜托你快醒来啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191165V#813F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x010A, 0x03, 0x00, 0x000003E8)
    OP_99(0x010A, 0x00, 0x03, 0x000003E8)
    ClearChrFlags(0x0008, 0x0080)
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0008)
    SetChrFlags(0x0008, 0x0080)
    OP_99(0x010A, 0x03, 0x07, 0x000003E8)
    Sleep(1000)

    OP_99(0x010A, 0x07, 0x09, 0x000003E8)
    Sleep(500)

    OP_99(0x010A, 0x09, 0x0D, 0x000003E8)
    Sleep(500)

    OP_99(0x010A, 0x0D, 0x13, 0x000003E8)
    OP_99(0x010A, 0x10, 0x13, 0x000003E8)

    ChrTalk(
        0x010A,
        (
            '#0120191166V#814F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191167V……嗯～\n',
            '怎么回事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191168V难道说，\n',
            '昨天的袭击只是一场梦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191169V#5P#1007F我也希望是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191170V但既然我们两人都记得，\n',
            '应该不可能是梦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x010A, 0x07, 0x09, 0x000003E8)

    ChrTalk(
        0x010A,
        (
            '#0120191171V#819F#6P啊～原来如此啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191172V呀～这次姐姐\n',
            '可真是败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191173V#5P#1019F亚妮拉丝……\n',
            '还在犯迷糊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x010A, 65535)
    SetChrSubChip(0x010A, 0)
    ClearChrFlags(0x010A, 0x0002)
    SetChrFlags(0x010A, 0x0001)
    SetChrPos(0x0101, -20730, 0, -19460, 68)
    SetChrPos(0x010A, -19800, 0, -18290, 159)
    ClearMapFlags(0x00000001)
    OP_6D(-24650, 0, -20010, 0)
    OP_67(0, 12770, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(179000, 0)
    OP_6E(262, 0)
    OP_1D(0x15)
    OP_C8(0x0200, 0x0046, 'C_PLAC02._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0BD5')
    def lambda_0BD5():
        OP_6D(-19150, 0, -18900, 6000)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_0BD5)

    @scena.Lambda('lambda_0BED')
    def lambda_0BED():
        OP_67(0, 12770, -10000, 6000)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0BED)

    @scena.Lambda('lambda_0C05')
    def lambda_0C05():
        OP_6C(15000, 6000)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_0C05)

    @scena.Lambda('lambda_0C15')
    def lambda_0C15():
        OP_8C(0x0101, 190, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0C15)

    @scena.Lambda('lambda_0C23')
    def lambda_0C23():
        OP_8C(0x010A, 90, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C23)

    WaitForThreadExit(0x010A, 0x0000)
    WaitForThreadExit(0x010A, 0x0001)
    Sleep(100)

    @scena.Lambda('lambda_0C40')
    def lambda_0C40():
        OP_8C(0x0101, 245, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0C40)

    @scena.Lambda('lambda_0C4E')
    def lambda_0C4E():
        OP_8C(0x010A, 92, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C4E)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x010A, 0x0000)
    WaitForThreadExit(0x010A, 0x0001)
    WaitForThreadExit(0x010A, 0x0002)
    Fade(1000)
    OP_6D(-21320, 0, -19030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_8C(0x010A, 172, 500)
    Sleep(100)

    OP_8C(0x0101, 102, 500)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120191174V#817F#2P嗯，首先\n',
            '试着把状况汇总一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191175V#812F昨天夜里，貌似猎兵团的集团\n',
            '袭击了宿舍……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191176V克鲁茨前辈受了伤，\n',
            '在我们急忙赶到后，\n',
            '敌人就紧接着从窗户闯入……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191177V然后我们两个\n',
            '马上被弄昏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191178V#1002F#5P嗯。\n',
            '和我的记忆一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191179V问题是，怎么会在这种地方\n',
            '醒过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 2, 0x1042)),
            Expr.Return,
        ),
        'loc_F1C',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191180V#812F#2P嗯，确实很奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191181V携带品之类的\n',
            '倒是没遗失的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191182V<FIXME>訓練の時に使っていた\n',
            '武具を取られちゃったみたい。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191183V#1004F#5P我、我也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191184V#1015F这么说来，把我们\n',
            '搬来这里的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1021')

    def _loc_F1C(): pass

    label('loc_F1C')

    ChrTalk(
        0x010A,
        (
            '#0120191180V#812F#2P嗯，确实很奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191181V携带品之类的\n',
            '倒是没遗失的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191187V<FIXME>昨日の夜に、身に付けていた\n',
            '武具は全部取られちゃったみたい。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191183V#1004F#5P我、我也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191184V#1015F这么说来，把我们\n',
            '搬来这里的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1021(): pass

    label('loc_1021')

    FadeOut(300, 0, 100)

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

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '把艾丝蒂尔她们搬到森林的是？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【克鲁茨】\n'),
            TXT(0x01, '【来袭的猎兵团】\n'),
            TXT(0x02, '【除此以外的第三者】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_10DD'),
        (0x00000001, 'loc_1247'),
        (0x00000002, 'loc_12D5'),
        (-1, 'loc_1387'),
    )

    def _loc_10DD(): pass

    label('loc_10DD')

    ChrTalk(
        0x010A,
        (
            '#0120191190V#813F#2P……这个可能性应该很低。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191191V就算是前辈，在那种状况下\n',
            '也不可能搬得动我们两个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191192V#1003F#5P的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191193V而且如果是克鲁茨前辈的话，\n',
            '就不会夺取我们的装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191194V#812F#2P最有可能的\n',
            '是来袭的猎兵团……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191195V但如果是这样，不把我们捆起来，\n',
            '而是就这么丢在这里的理由就很不符合逻辑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1387')

    def _loc_1247(): pass

    label('loc_1247')

    OP_2B(0x007E, 0x0003)

    ChrTalk(
        0x010A,
        (
            '#0120191196V#812F#2P嗯……\n',
            '虽然一般都会这么想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191197V但是，不把我们捆起来，\n',
            '而是就这么丢在这里的理由就很不符合逻辑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1387')

    def _loc_12D5(): pass

    label('loc_12D5')

    ChrTalk(
        0x010A,
        (
            '#0120191198V#1316F#2P嗯……\n',
            '倒也不是不可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191199V#812F最有可能的\n',
            '是来袭的猎兵团。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191197V只是，不把我们捆起来，\n',
            '而是就这么丢在这里的理由就很不符合逻辑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1387')

    def _loc_1387(): pass

    label('loc_1387')

    ChrTalk(
        0x0101,
        (
            '#0010191201V#1002F#5P把昏倒的我们\n',
            '运来这里并解除武装之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191202V或许发生了什么意外，\n',
            '急忙转移到别的地方了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191203V#816F#2P原来如此。\n',
            '这或许很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191204V若是这样，在这里久留\n',
            '似乎也很危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191205V艾丝蒂尔，你带了地图吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191206V#1004F#5P啊，嗯。\n',
            '因为行李没被拿走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191207V#1006F……有了有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD(0x002400A0, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName('亚妮拉丝')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0120191208V#810F嗯，果然没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191209V这里就是昨天用来训练的\n',
            '『圣科洛瓦森林』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 340, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010191210V#1015F这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191211V当前的目的就是要逃出森林，\n',
            '并确认宿舍的情况吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName('亚妮拉丝')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0120191212V#813F嗯，虽然也很在意\n',
            '前辈的安危等一些事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191213V但首先必须要打破现状才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)

    OP_AE(0x000003E8)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 2, 0x1042)),
            Expr.Return,
        ),
        'loc_1732',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191214V#810F#4P<FIXME>それじゃあ、出発しようか。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191215V敵が近くにいるかもしれないし、\n',
            '慎重に行動した方がいいね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191216V#1002F#5P嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1804')

    def _loc_1732(): pass

    label('loc_1732')

    ChrTalk(
        0x010A,
        (
            '#0120191214V#810F#4P<FIXME>それじゃあ、出発しようか。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191218V丸腰に近い状態だから\n',
            '慎重に行動した方がいいね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191219V#1002F#5P嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191220V要是能设法取回\n',
            '被卸下的装备就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1804(): pass

    label('loc_1804')

    OP_A2(0x100D)
    OP_28(0x007F, 0x01, 0x0002)
    OP_28(0x007F, 0x01, 0x0004)
    OP_28(0x007F, 0x01, 0x0008)
    OP_28(0x007F, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x1822
@scena.Code('func_05_1822')
def func_05_1822():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 6, 0x100E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1831',
    )

    Call(0, 0x0006)

    Jump('loc_1835')

    def _loc_1831(): pass

    label('loc_1831')

    Call(0, 0x0007)

    def _loc_1835(): pass

    label('loc_1835')

    Return()

# id: 0x0006 offset: 0x1836
@scena.Code('func_06_1836')
def func_06_1836():
    EventBegin(0x00)
    Fade(1000)
    OP_6D(-28980, 0, -18140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -27880, 0, -18520, 325)
    SetChrPos(0x010A, -28610, 0, -19090, 350)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010191221V#1002F这个果然\n',
            '是猎兵团使用过的帐篷吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191222V#812F可能性很高的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191223V总之先调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到5个',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['中回复药'], 5)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到2个',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['EP填充剂Ⅰ'], 2)

    ChrTalk(
        0x0101,
        (
            '#0010191224V#1007F嗯……\n',
            '除此之外没有别的东西了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191225V#1015F要是我们的\n',
            '装备在就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191226V#1316F看来没那么简单呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191227V#810F不过，帐篷的状况很不错，\n',
            '或许可以用来休息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191228V虽然没多少空闲时间，\n',
            '但要是累了就回来这里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191229V#1011F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x100E)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1ADE
@scena.Code('func_07_1ADE')
def func_07_1ADE():
    TalkBegin(0x00FF)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
            TXT(0x00, '【稍微休息一下】\n'),
            TXT(0x01, '【不休息】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B4C'),
        (0x00000001, 'loc_1C20'),
        (-1, 'loc_1C23'),
    )

    def _loc_1B4C(): pass

    label('loc_1B4C')

    OP_1F(0x00, 0x00000BB8)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    Sleep(3500)

    OP_1E()
    OP_6D(-28380, 0, -18660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -28380, 0, -18660, 135)
    SetChrPos(0x010A, -28380, 0, -18660, 135)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            'ＨＰ和ＥＰ恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1F(0x64, 0x000003E8)
    FadeIn(1000, 0)
    OP_0D()

    Jump('loc_1C23')

    def _loc_1C20(): pass

    label('loc_1C20')

    Jump('loc_1C23')

    def _loc_1C23(): pass

    label('loc_1C23')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
