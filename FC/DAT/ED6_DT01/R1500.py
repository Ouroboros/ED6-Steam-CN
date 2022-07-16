import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '红发的青年'),
    TXT(0x02, '拉文努村'),
    TXT(0x03, '西柏斯街道方向'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1500.x'
    header.mapIndex       = 59
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xFF5
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
            word_3A         = 59,
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
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT09/CH10030._CH', 'ED6_DT09/CH10030P._CP'),
        ('ED6_DT09/CH10031._CH', 'ED6_DT09/CH10031P._CP'),
        ('ED6_DT09/CH10330._CH', 'ED6_DT09/CH10330P._CP'),
        ('ED6_DT09/CH10331._CH', 'ED6_DT09/CH10331P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 2000,
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
            x                   = -170710,
            z                   = 12010,
            y                   = 95390,
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
        ScenaNpcData(
            x                   = -204960,
            z                   = -100,
            y                   = -46530,
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

# id: 0x10003 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -191470,
            z           = 3990,
            y           = 18830,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -180300,
            z           = 3990,
            y           = -3330,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -166330,
            z           = 11950,
            y           = 8590,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x196
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -210250,
            y           = -5000,
            z           = -8632,
            range       = -197450,
            dword_10    = 0x00001388,
            dword_14    = 0xFFFFD3FA,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x1B6
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1B6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1B7
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -300000, -103000, 196639)

    Return()

# id: 0x0002 offset: 0x1CA
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1DF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_1DF(): pass

    label('loc_1DF')

    Return()

# id: 0x0003 offset: 0x1E0
@scena.Code('func_03_1E0')
def func_03_1E0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 1, 0x319)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_FEC',
    )

    SetScenaFlags(ScenaFlag(0x0063, 1, 0x319))
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0000, 0x0008, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -192020, 3600, 10030, 223)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010021459V#004F那是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB')

    def _loc_25A(): pass

    label('loc_25A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_283',
    )

    ChrTalk(
        0x0102,
        (
            '#0020021460V#014F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030021461V#023F哎呀……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AB(): pass

    label('loc_2AB')

    @scena.Lambda('lambda_02B1')
    def lambda_02B1():
        CameraMove(-197690, 1800, 1790, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_02B1)

    @scena.Lambda('lambda_02C9')
    def lambda_02C9():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_02C9)

    Sleep(500)

    @scena.Lambda('lambda_02DE')
    def lambda_02DE():
        ChrWalkTo(0x00FE, -196710, 2050, 2880, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_02DE)

    Sleep(2000)

    WaitForThreadExit(0x0008, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021462V#052F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0103, -205000, 1920, -8810, 22)
    SetChrPos(0x0101, -205000, 1920, -8810, 22)
    SetChrPos(0x0102, -205000, 1920, -8810, 22)

    @scena.Lambda('lambda_0375')
    def lambda_0375():
        ChrWalkTo(0x00FE, -197790, 2050, -120, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0375)

    Sleep(500)

    @scena.Lambda('lambda_0395')
    def lambda_0395():
        ChrWalkTo(0x00FE, -199700, 1950, -40, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0395)

    Sleep(500)

    @scena.Lambda('lambda_03B5')
    def lambda_03B5():
        ChrWalkTo(0x00FE, -199770, 2009, -1760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03B5)

    WaitForThreadExit(0x0103, 0x0001)
    SetChrDirection(0x0103, 0, 0)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrDirection(0x0101, 45, 0)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 0, 0)

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021463V#050F是雪拉扎德啊。\n',
            '没想到竟然在这里见到你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021464V#020F那正是我要说的台词。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021465V本来以为你在王都呢。\n',
            '你也是来调查这个事件的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021466V#053F不，只是些琐事而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021467V#050F对了，\n',
            '据说这个事件是空贼干的好事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021468V既然你也来到这里，\n',
            '那我就安心交给你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021469V要好好努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021470V#022F什么呀，你也太无情了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021471V老师他可能被别人抓住了，\n',
            '你也应该听说了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021472V#052F#051F被抓住了？\n',
            '那个卡西乌斯·布莱特吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021473V哈哈哈，别开玩笑了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021474V那个战无不胜的大叔\n',
            '怎么可能给那帮空贼占上风！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021475V肯定是哪里搞错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021476V#025F虽然我也是这么想的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021477V#002F（这家伙是干什么的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021478V#010F（我也不知道……\n',
            '　但肯定是游击士没错。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021479V#050F顺便问一下……\n',
            '这两个小鬼是干什么的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021480V看上去像是刚加入的新人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021481V#021F呵呵，听了可别吃惊哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021482V他们是卡西乌斯老师的孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021483V#052F这还真是让人惊讶……\n',
            '是那个大叔的孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021484V哼～这两个小鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -198060, 2029, 1420, 2000, 0x00)

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021485V#057F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021486V#004F怎、怎么了？\n',
            '盯着我们来回看个没完……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021487V#050F#1P黑发的小子暂且不论……\n',
            '那边梳辫子的小丫头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021488V#050F她真是大叔的女儿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021489V#005F你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021490V#010F她的确是如假包换的\n',
            '卡西乌斯·布莱特的亲生女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021491V我才是养子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021492V#052F#1P哦～是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021493V#053F算了，这种事情怎么样都无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021494V#009F才、才不是怎么样都无所谓！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 180, 400)

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021495V#051F#1P那就再会了，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021496V不要让这两个小鬼拖了后腿，\n',
            '总之多多保重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021497V#027F是是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021498V你也要注意别冒失行动，\n',
            '以免遭受沉重的打击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '红发的青年',
        (
            '#0050021499V#051F#1P哈哈，铭记在心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0040)

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_C43',
    )

    ChrTalk(
        0x0008,
        (
            '#0050021500V#050F#1P对了，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021501V废坑那边被通缉的魔兽\n',
            '是你除掉的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021502V#020F#1P对，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021503V但是严格说来是『我们』才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050021504V#053F#1P哈哈，用新人来凑数\n',
            '也是没有办法的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021505V#053F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021506V#051F那么，就保持这个水准，\n',
            '搜索空贼的行动也要加油哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050021507V再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C43(): pass

    label('loc_C43')

    @scena.Lambda('lambda_0C49')
    def lambda_0C49():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0C49')

    DispatchAsync2(0x0101, 0x0002, lambda_0C49)

    @scena.Lambda('lambda_0C5A')
    def lambda_0C5A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0C5A')

    DispatchAsync2(0x0102, 0x0002, lambda_0C5A)

    @scena.Lambda('lambda_0C6B')
    def lambda_0C6B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0C6B')

    DispatchAsync2(0x0103, 0x0002, lambda_0C6B)

    @scena.Lambda('lambda_0C7C')
    def lambda_0C7C():
        CameraMove(-198470, 2000, 160, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C7C)

    ChrWalkTo(0x0008, -199870, 1970, 1280, 3000, 0x00)
    ChrWalkTo(0x0008, -200920, 1850, 200, 3000, 0x00)
    ChrWalkTo(0x0008, -202280, 1840, -9440, 3000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010021508V#005F#1P那、那家伙是谁呀！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021509V太过分了，\n',
            '真是气死我了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021510V#010F原来如此……\n',
            '刚才那个人是『重剑阿加特』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021511V#004F#1P『重剑阿加特』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030021512V#020F阿加特·科洛斯纳。\n',
            '游击士协会的正游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021513V#020F没有特定的所属支部，\n',
            '活动范围遍布全国各地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021514V使用一把能将魔兽\n',
            '一刀斩成两段的超重大剑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021515V总而言之，就是相当的厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021516V#009F哼，先不说厉不厉害，\n',
            '是个没礼貌的家伙肯定没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021517V从刚才的谈话中看来，\n',
            '那家伙也是老爸认识的人吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 45, 400)

    ChrTalk(
        0x0102,
        (
            '#0020021518V#010F他虽然承认父亲的实力，\n',
            '但好像感觉不出什么善意的态度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021519V#026F以前发生了一些事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021520V所以和老师产生过冲突。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021521V#002F哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021522V算了，怎样都无所谓啦。\n',
            '那种没礼貌的家伙，我才不想管呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021523V我们赶快去拉文努村吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_FEC(): pass

    label('loc_FEC')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
